CREATE OR REPLACE PROCEDURE postgres.insert_unique(from_table varchar(50), from_column varchar(50), to_table varchar(50), to_column varchar(50)) LANGUAGE plpgsql AS $procedure$
	begin

execute 'insert into ' || to_table || '(' || to_column || ')
	(select distinct ' || from_column || ' 
		from ' || from_table || ' 
		where 
			not exists (select ' || to_column || ' from ' || to_table || ' )
		and 
			' || from_table || '.' || from_column || ' is not null);';

	END;
$procedure$;

;


CREATE OR REPLACE PROCEDURE postgres.insert_vitals() LANGUAGE plpgsql AS $procedure$
declare
	arow RECORD;
	before_ BIGINT;
	after_ BIGINT;

begin
	for arow in select * from temp_vitals loop
		raise INFO 'arow:%', arow;
		if arow."date" is null or arow."date" = '' then
			continue;
		end if;
		-- Region before measure insert
		if arow.before_timestamp is not null then
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
				(select "id" from "m_judgements" where "description" = arow.before_judge_name),
				(select "id" from "m_fatigue_scores" where "description" = arow.before_fatigue_score_name),
				(select "id" from "m_fatigue_levels" where "description" = arow.before_fatigue_level_name)
			)
			returning id into before_;
		else
			before_ := null;
		end if;
		raise INFO 'before id:%', before_;
		-- Region after measure insert
		if arow.after_timestamp is not null then
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
				(select "id" from "m_judgements" where "description" = arow.after_judge_name),
				(select "id" from "m_fatigue_scores" where "description" = arow.after_fatigue_score_name),
				(select "id" from "m_fatigue_levels" where "description" = arow.after_fatigue_level_name)
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
			arow."date",
			(select id from "m_companies" where "code" = arow.company_id),
			(select id from "m_offices" where "code" = arow.office_id),
			(select id from "m_users" where "code" = arow.user_id),
			(select id from "m_crew_judge_types"  where "description" = arow.before_crew_judge_name),
			(select id from "m_crew_judge_reasons" where "description" = arow.before_crew_judge_reason_name)
		);
	end loop;
end;
$procedure$;

;


CREATE OR REPLACE PROCEDURE postgres.insert_events() LANGUAGE plpgsql AS $procedure$
declare
	arow RECORD;

begin
	for arow in select * from temp_events loop
		raise INFO 'arow:%', arow;
		insert into t_events (
			"date",
			"timestamp",
			"company_id",
			"office_id",
			"car_number_id",
			"user_id",
			"type_id",
			"latitude",
			"longitude",
			"video_file_name1",
			"video_file_name2",
			"d_kbn")
		values (
			arow."date"::timestamptz,
			arow."timestamp"::timestamptz,
			(select id from "m_companies" where "code" = arow.company_id),
			(select id from "m_offices" where "code" = arow.office_id),
			(select id from "m_car_numbers" where "code" = arow.car_number),
			(select id from "m_users" where "code" = arow.user_id),
			(select id from "m_event_types" where "code" = arow.event_id),
			arow.latitude,
			arow.longitude,
			arow.videofilename1,
			arow.videofilename2,
			arow.d_kbn
		);
	end loop;
end;
$procedure$;

;


CREATE OR REPLACE PROCEDURE postgres.insert_sensors_map() LANGUAGE plpgsql AS $procedure$
declare
	arow RECORD;

begin
	for arow in select * from temp_sensors_map loop
		insert into t_positions (
			"date",
			"timestamp",
			"company_id",
			"office_id",
			"car_number_id",
			"user_id",
			"latitude",
			"longitude",
			"speed",
			"mapped_latitude",
			"mapped_longitude",
			"distance",
			"d_kbn")
		values (
			arow."date"::timestamptz,
			arow."timestamp"::timestamptz,
			(select id from "m_companies" where "code" = arow.company_id),
			(select id from "m_offices" where "code" = arow.office_id),
			(select id from "m_car_numbers" where "code" = arow.car_number),
			(select id from "m_users" where "code" = arow.user_id),
			arow.latitude,
			arow.longitude,
			arow.speed,
			arow.mapped_latitude,
			arow.mapped_longitude,
			arow.distance,
			arow.d_kbn
		);
	end loop;
end;
$procedure$;

;

