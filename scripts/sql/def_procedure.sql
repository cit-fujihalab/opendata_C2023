CREATE OR REPLACE PROCEDURE postgres.insert_unique(from_table varchar(50), from_column varchar(50), to_table varchar(50), to_column varchar(50)) LANGUAGE plpgsql AS $procedure$
	begin

execute 'insert into ' || to_table || '(' || to_column || ')' ||
'(select distinct ' || from_column ||
'  from ' || from_table || '
where not exists (select 
	' || to_column ||
'  from 
	' || to_table || '
  where
	' || from_table || '.' || from_column || ' = ' || to_table || '.' || to_column || '));';

	END;
$procedure$;

;


CREATE OR REPLACE PROCEDURE postgres.insert_vitals() LANGUAGE plpgsql AS $procedure$
declare
	arow RECORD;
	before_ BIGINT;
	after_ BIGINT;

begin
	for arow in select * from temp1 loop
		raise INFO 'arow:%', arow;
		-- Region before measure insert
		if arow.before_timestamp is not null and not arow.before_timestamp = '' then
			insert into t_measurements (
				"timestamp",
				"body_temp",
				"spo2",
				"sys",
				"dia",
				"fatigue_lh",
				"fatigue_deviation",
				"cnt",
				"judge_id",
				"fatigue_score_id",
				"fatigue_level_id")
			values (
				arow.before_timestamp::timestamptz,
				arow.before_body_temp,
				arow.before_spo2,
				arow.before_sys,
				arow.before_dia,
				arow.before_fatigue_lh,
				arow.before_fatigue_deviation,
				arow.before_cnt,
				(select "id" from "m_judgements" where "code" = arow.before_judge_id),
				(select "id" from "m_fatigue_scores" where "code" = arow.before_fatigue_score_id),
				(select "id" from "m_fatigue_levels" where "code" = arow.before_fatigue_level_id)
			)
			returning id into before_;
		else
			before_ := null;
		end if;
		raise INFO 'before id:%', before_;
		-- Region after measure insert
		if arow.after_timestamp is not null and not arow.after_timestamp = '' then
			insert into t_measurements (
				"timestamp",
				"body_temp",
				"spo2",
				"sys",
				"dia",
				"fatigue_lh",
				"fatigue_deviation",
				"cnt",
				"judge_id",
				"fatigue_score_id",
				"fatigue_level_id")
			values (
				arow.after_timestamp::timestamptz,
				arow.after_body_temp,
				arow.after_spo2,
				arow.after_sys,
				arow.after_dia,
				arow.after_fatigue_lh,
				arow.after_fatigue_deviation,
				arow.after_cnt,
				(select "id" from "m_judgements" where "code" = arow.after_judge_id),
				(select "id" from "m_fatigue_scores" where "code" = arow.after_fatigue_score_id),
				(select "id" from "m_fatigue_levels" where "code" = arow.after_fatigue_level_id)
			)
			returning id into after_;
		else
			after_ := null;
		end if;
		raise INFO 'after_id:%', after_;
		-- Region vital insert
		insert into t_vitals (
			"before_measurement_id",
			"after_measurement_id",
			"date",
			"company_id",
			"office_id",
			"user_id",
			"before_crew_judge_id",
			"before_crew_judge_reason_id")
		values (
			before_,
			after_,
			arow."date"::timestamptz,
			(select id from "m_companies" where "code" = arow.company_id),
			(select id from "m_offices" where "code" = arow.office_id),
			(select id from "m_users" where "code" = arow.user_id),
			(select id from "m_crew_judge_types"  where "code" = arow.before_crew_judge_id),
			(select id from "m_crew_judge_reasons" where "code" = arow.before_crew_judge_reason_id)
		);
	end loop;
end;
$procedure$;

;

