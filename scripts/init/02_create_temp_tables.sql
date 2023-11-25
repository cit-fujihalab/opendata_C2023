SET temp_tablespaces='tbsp_z';

CREATE TABLE postgres.temp_driving_vitals (
	"date" varchar(8) NULL,
	company_id varchar(7) NULL,
	office_id varchar(12) NULL,
	car_number varchar(20) NULL,
	user_id varchar(30) NULL,
	"timestamp" timestamptz NULL,
	fatigue_score_id varchar(4) NULL,
	fatigue_score_name varchar(50) NULL,
	fatigue_level_id varchar(4) NULL,
	fatigue_level_name varchar(50) NULL
) TABLESPACE tbsp_z;

CREATE TABLE postgres.temp_events (
	"date" varchar(8) NULL,
	company_id varchar(7) NULL,
	office_id varchar(12) NULL,
	car_number varchar(20) NULL,
	user_id varchar(30) NULL,
	"timestamp" timestamptz NULL,
	event_id varchar(10) NULL,
	event_name varchar(20) NULL,
	latitude float8 NULL,
	longitude float8 NULL,
	d_kbn int2 NULL,
	videofilename1 varchar(70) NULL,
	videofilename2 varchar(70) NULL
) TABLESPACE tbsp_z;

CREATE TABLE postgres.temp_sensors_map (
	"date" varchar(8) NULL,
	company_id varchar(7) NULL,
	office_id varchar(12) NULL,
	car_number varchar(20) NULL,
	user_id varchar(30) NULL,
	"timestamp" timestamptz NULL,
	latitude float8 NULL,
	longitude float8 NULL,
	speed float4 NULL,
	mapped_latitude float8 NULL,
	mapped_longitude float8 NULL,
	distance float8 NULL,
	d_kbn varchar(1) NULL
) TABLESPACE tbsp_z;

CREATE TABLE postgres.temp_vitals (
	"date" varchar(8) NULL,
	company_id varchar(7) NULL,
	office_id varchar(12) NULL,
	user_id varchar(30) NULL,
	before_timestamp timestamptz NULL,
	before_judge_id varchar(4) NULL,
	before_judge_name varchar(20) NULL,
	before_body_temp float4 NULL,
	before_spo2 float4 NULL,
	before_sys float4 NULL,
	before_dia float4 NULL,
	before_fatigue_score_id varchar(4) NULL,
	before_fatigue_score_name varchar(30) NULL,
	before_fatigue_level_id varchar(4) NULL,
	before_fatigue_level_name varchar(20) NULL,
	before_fatigue_lh float4 NULL,
	before_fatigue_deviation float4 NULL,
	before_cnt int2 NULL,
	before_crew_judge_id varchar(4) NULL,
	before_crew_judge_name varchar(10) NULL,
	before_crew_judge_reason_id varchar(4) NULL,
	before_crew_judge_reason_name varchar(50) NULL,
	after_timestamp timestamptz NULL,
	after_judge_id varchar(4) NULL,
	after_judge_name varchar(20) NULL,
	after_body_temp float4 NULL,
	after_spo2 float4 NULL,
	after_sys float4 NULL,
	after_dia float4 NULL,
	after_fatigue_score_id varchar(4) NULL,
	after_fatigue_score_name varchar(30) NULL,
	after_fatigue_level_id varchar(4) NULL,
	after_fatigue_level_name varchar(20) NULL,
	after_fatigue_lh float4 NULL,
	after_fatigue_deviation float4 NULL,
	after_cnt int2 NULL
) TABLESPACE tbsp_z;

CREATE OR REPLACE VIEW temp_dv AS
	SELECT 
		tdv."date" "date",
		tdv."timestamp" "timestamp",
		mc.id "company_id",
		mo.id "office_id",
		mcn.id "car_number_id",
		mu.id "user_id",
		mfs.id "fatigue_score_id",
		mfl.id "fatigue_level_id"
	FROM temp_driving_vitals tdv
	LEFT OUTER JOIN m_companies mc ON mc.code = tdv.company_id
	LEFT OUTER JOIN m_offices mo ON mo.code = tdv.office_id
	LEFT OUTER JOIN m_car_numbers mcn ON mcn.code = tdv.car_number
	LEFT OUTER JOIN m_users mu ON mu.code = tdv.user_id
	LEFT OUTER JOIN m_fatigue_scores mfs ON mfs.description = tdv.fatigue_score_name
	LEFT OUTER JOIN m_fatigue_levels mfl ON mfl.description = tdv.fatigue_level_name;

CREATE OR REPLACE VIEW temp_ev AS 
	SELECT 
		tev."date" "date",
		tev."timestamp" "timestamp",
		mc.id "company_id",
		mo.id "office_id",
		mcn.id "car_number_id",
		mu.id "user_id",
		met.id "type_id",
		tev.latitude,
		tev.longitude,
		tev.videofilename1 "video_file_name1",
		tev.videofilename2 "video_file_name2",
		tev.d_kbn
	FROM temp_events tev
	LEFT OUTER JOIN m_companies mc ON mc.code = tev.company_id
	LEFT OUTER JOIN m_offices mo ON mo.code = tev.office_id
	LEFT OUTER JOIN m_car_numbers mcn ON mcn.code = tev.car_number
	LEFT OUTER JOIN m_users mu ON mu.code = tev.user_id
	LEFT OUTER JOIN m_event_types met ON met.code = tev.event_id;

CREATE OR REPLACE VIEW temp_vt AS
	SELECT 
		tv."date",
		mc.id "company_id",
		mo.id "office_id",
		mu.id "user_id",
		tv.before_timestamp,
		bmj.id "before_judge_id",
		tv.before_body_temp,
		tv.before_spo2,
		tv.before_sys,
		tv.before_dia,
		bmfs.id "before_fatigue_score_id",
		bmfl.id "before_fatigue_level_id",
		tv.before_fatigue_lh,
		tv.before_fatigue_deviation,
		tv.before_cnt,
		mcj.id "before_crew_judge_id",
		mcjr.id "before_crew_judge_reason_id",
		tv.after_timestamp,
		amj.id "after_judge_id",
		tv.after_body_temp,
		tv.after_spo2,
		tv.after_sys,
		tv.after_dia,
		amfs.id "after_fatigue_score_id",
		amfl.id "after_fatigue_level_id",
		tv.after_fatigue_lh,
		tv.after_fatigue_deviation,
		tv.after_cnt
	FROM temp_vitals tv
	LEFT OUTER JOIN m_companies mc ON mc.code = tv.company_id
	LEFT OUTER JOIN m_offices mo ON mo.code = tv.office_id
	LEFT OUTER JOIN m_users mu ON mu.code = tv.user_id
	LEFT OUTER JOIN m_judgements bmj ON bmj.code = tv.before_judge_id
	LEFT OUTER JOIN m_fatigue_scores bmfs ON bmfs.description = tv.before_fatigue_score_name
	LEFT OUTER JOIN m_fatigue_levels bmfl ON bmfl.description = tv.before_fatigue_level_name
	LEFT OUTER JOIN m_crew_judge_types mcj ON mcj.code = tv.before_crew_judge_id
	LEFT OUTER JOIN m_crew_judge_types mcjr ON mcjr.code = tv.before_crew_judge_reason_id
	LEFT OUTER JOIN m_judgements amj ON amj.code = tv.after_judge_id
	LEFT OUTER JOIN m_fatigue_scores amfs ON amfs.description = tv.after_fatigue_score_name
	LEFT OUTER JOIN m_fatigue_levels amfl ON amfl.description = tv.after_fatigue_level_name;

CREATE OR REPLACE PROCEDURE postgres.insert_unique(IN from_table character varying, IN from_column character varying, IN to_table character varying, IN to_column character varying)
 LANGUAGE plpgsql
AS $procedure$
BEGIN
	raise INFO '[%] from_table: % to_table: %', pg_backend_pid(), from_table, to_table;
	EXECUTE 'INSERT INTO ' || to_table || '(' || to_column || ')
		(SELECT DISTINCT (' || from_column || ') FROM ' || from_table || ' WHERE ' || from_column || ' IS NOT NULL) 
		ON CONFLICT DO NOTHING;';
END;
$procedure$;

CREATE OR REPLACE PROCEDURE postgres.insert_file(IN file_name CHARACTER VARYING) LANGUAGE plpgsql AS $procedure$
DECLARE
	temp_id varchar;
BEGIN
	SET work_mem to '10GB';
	raise INFO '[%] loading file: %', pg_backend_pid(), file_name;
	SET temp_tablespaces='tbsp_z';

	temp_id = '_' || replace(gen_random_uuid()::varchar,'-', '_');
	EXECUTE 'CREATE UNLOGGED TABLE temp_sensors_map' || temp_id || ' (LIKE temp_sensors_map) TABLESPACE tbsp_z;';
	EXECUTE 'TRUNCATE temp_sensors_map' || temp_id || ' CONTINUE IDENTITY RESTRICT;';
	EXECUTE 'COPY temp_sensors_map' || temp_id || ' from ''' || file_name || ''' with csv header encoding ''UTF8'';';

	CALL insert_unique('temp_sensors_map' || temp_id, 'company_id', 'm_companies', 'code');
	CALL insert_unique('temp_sensors_map' || temp_id, 'office_id', 'm_offices', 'code');
	CALL insert_unique('temp_sensors_map' || temp_id, 'car_number', 'm_car_numbers', 'code');
	CALL insert_unique('temp_sensors_map' || temp_id, 'user_id', 'm_users', 'code');
	raise INFO '[%] master prepared', pg_backend_pid();

	EXECUTE 'WITH drive_joined AS (
		SELECT
			"mu"."id",
			"mo"."office_id",
			"mcn"."id",
			"mc"."id"
		FROM "temp_sensors_map' || temp_id || '" AS "tsm"
		INNER JOIN "m_offices" "mo" ON "mo"."code" = "tsm"."office_id"
		INNER JOIN "m_users" "mu" ON "mu"."code" = "tsm"."user_id"
		INNER JOIN "m_companies" "mc" ON "mc"."code" = "tsm"."company_id"
		INNER JOIN "m_car_numbers" "mcn" ON "mcn"."code" = "tsm"."car_number"
	)
	INSERT INTO "t_drive" ("user_id", "car_number_id", "company_id")
	SELECT * FROM drive_joined
	ON CONFLICT DO NOTHING;';

	EXECUTE 'INSERT INTO t_positions (
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
		SELECT * FROM (
			SELECT 
			tsm."date" "date",
			tsm."timestamp" "timestamp",
			mc.id "company_id",
			mo.id "office_id",
			mcn.id "car_number_id",
			mu.id "user_id",
			tsm.latitude,
			tsm.longitude,
			tsm.speed,
			tsm.mapped_latitude,
			tsm.mapped_longitude,
			tsm.distance,
			tsm.d_kbn 
			FROM temp_sensors_map' || temp_id || ' tsm
			LEFT OUTER JOIN m_companies mc ON mc.code = tsm.company_id
			LEFT OUTER JOIN m_offices mo ON mo.code = tsm.office_id
			LEFT OUTER JOIN m_car_numbers mcn ON mcn.code = tsm.car_number
			LEFT OUTER JOIN m_users mu ON mu.code = tsm.user_id
		) temp_pos;';
	EXECUTE 'DROP TABLE temp_sensors_map' || temp_id || ';';
	raise INFO '[%] loaded file: %', pg_backend_pid(), file_name;
END;
$procedure$;
