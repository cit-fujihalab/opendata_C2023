SET work_mem to '16GB';
SET temp_tablespaces='tbsp_z';

CALL insert_unique('temp_driving_vitals', 'company_id', 'm_companies', 'code');
CALL insert_unique('temp_driving_vitals', 'office_id', 'm_offices', 'code');
CALL insert_unique('temp_driving_vitals', 'car_number', 'm_car_numbers', 'code');
CALL insert_unique('temp_driving_vitals', 'user_id', 'm_users', 'code');
CALL insert_unique('temp_driving_vitals', 'fatigue_score_name', 'm_fatigue_scores', 'description');
CALL insert_unique('temp_driving_vitals', 'fatigue_level_name', 'm_fatigue_levels', 'description');

CALL insert_unique('temp_events', 'company_id', 'm_companies', 'code');
CALL insert_unique('temp_events', 'office_id', 'm_offices', 'code');
CALL insert_unique('temp_events', 'car_number', 'm_car_numbers', 'code');
CALL insert_unique('temp_events', 'user_id', 'm_users', 'code');
CALL insert_unique('temp_events', 'event_id', 'm_event_types', 'code');

CALL insert_unique('temp_vitals', 'company_id', 'm_companies', 'code');
CALL insert_unique('temp_vitals', 'office_id', 'm_offices', 'code');
CALL insert_unique('temp_vitals', 'user_id', 'm_users', 'code');
CALL insert_unique('temp_vitals', 'before_judge_id', 'm_judgements', 'code');
CALL insert_unique('temp_vitals', 'after_judge_id', 'm_judgements', 'code');
CALL insert_unique('temp_vitals', 'before_fatigue_score_name', 'm_fatigue_scores', 'description');
CALL insert_unique('temp_vitals', 'after_fatigue_score_name', 'm_fatigue_scores', 'description');
CALL insert_unique('temp_vitals', 'before_fatigue_level_name', 'm_fatigue_levels', 'description');
CALL insert_unique('temp_vitals', 'after_fatigue_level_name', 'm_fatigue_levels', 'description');
CALL insert_unique('temp_vitals', 'before_crew_judge_id', 'm_crew_judge_types', 'code');
CALL insert_unique('temp_vitals', 'before_crew_judge_reason_id', 'm_crew_judge_reasons', 'code');

INSERT INTO t_driving_vitals (
	"date",
	"timestamp",
	"company_id",
	"office_id",
	"car_number_id",
	"user_id",
	"fatigue_score_id",
	"fatigue_level_id")
	SELECT * FROM temp_dv;

INSERT INTO t_events (
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
	SELECT * FROM temp_ev;

CREATE OR REPLACE PROCEDURE postgres.insert_vitals() LANGUAGE plpgsql AS $procedure$
DECLARE
	arow RECORD;
	before_ BIGINT;
	after_ BIGINT;
BEGIN
	FOR arow IN SELECT * FROM temp_vt LOOP
		IF arow."date" IS NULL OR arow."date" = '' THEN
			continue;
		END IF;
		-- Region before measure insert
		IF arow.before_timestamp IS NOT NULL THEN
			INSERT INTO t_measurements (
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
			VALUES (
				arow.before_timestamp::timestamptz,
				arow.before_body_temp,
				arow.before_spo2,
				arow.before_sys,
				arow.before_dia,
				arow.before_fatigue_lh,
				arow.before_fatigue_deviation,
				arow.before_cnt,
				arow.before_judge_id,
				arow.before_fatigue_score_id,
				arow.before_fatigue_level_id
			)
			RETURNING id INTO before_;
		ELSE
			before_ := NULL;
		END IF;
		-- Region after measure insert
		IF arow.after_timestamp IS NOT NULL THEN
			INSERT INTO t_measurements (
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
			VALUES (
				arow.after_timestamp::timestamptz,
				arow.after_body_temp,
				arow.after_spo2,
				arow.after_sys,
				arow.after_dia,
				arow.after_fatigue_lh,
				arow.after_fatigue_deviation,
				arow.after_cnt,
				arow.after_judge_id,
				arow.after_fatigue_score_id,
				arow.after_fatigue_level_id
			)
			RETURNING id INTO after_;
		ELSE
			after_ := NULL;
		END IF;
		-- Region vital insert
		INSERT INTO t_vitals (
			"before_measurement_id",
			"after_measurement_id",
			"date",
			"company_id",
			"office_id",
			"user_id",
			"before_crew_judge_id",
			"before_crew_judge_reason_id")
		VALUES (
			before_,
			after_,
			arow."date",
			arow.company_id,
			arow.office_id,
			arow.user_id,
			arow.before_crew_judge_id,
			arow.before_crew_judge_reason_id
		);
	END LOOP;
END;
$procedure$;

CALL insert_vitals();
