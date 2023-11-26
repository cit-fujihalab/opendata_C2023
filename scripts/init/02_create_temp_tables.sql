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

CREATE UNLOGGED TABLE postgres.temp_sensors_map (
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
BEGIN
	-- SET work_mem to '5GB';
	SET temp_tablespaces='tbsp_z';

	CREATE TEMP TABLE temp_sensors_map_ (LIKE temp_sensors_map) TABLESPACE tbsp_z;
	TRUNCATE temp_sensors_map_ CONTINUE IDENTITY RESTRICT;

	raise INFO '[%] loading file: %', pg_backend_pid(), file_name;
	EXECUTE 'COPY temp_sensors_map_ from ''' || file_name || ''' with csv header encoding ''UTF8'';';
	ANALYZE temp_sensors_map_;
	raise INFO '[%] csv copied: %', pg_backend_pid(), file_name;

	WITH "master_unique_pre" AS (
		SELECT DISTINCT "company_id", "office_id", "car_number", "user_id" FROM temp_sensors_map_
	),
	"companies" AS (
		INSERT INTO m_companies ("code") 
			SELECT DISTINCT ("company_id") FROM master_unique_pre
			ON CONFLICT ("code") DO UPDATE SET "code"=EXCLUDED."code"
			RETURNING *
	),
	"offices" AS (
		INSERT INTO m_offices ("code") 
			SELECT DISTINCT ("office_id") FROM master_unique_pre
			ON CONFLICT ("code") DO UPDATE SET "code"=EXCLUDED."code"
			RETURNING *
	),
	"car_numbers" AS (
		INSERT INTO m_car_numbers ("code") 
			SELECT DISTINCT ("car_number") FROM master_unique_pre
			ON CONFLICT ("code") DO UPDATE SET "code"=EXCLUDED."code"
			RETURNING *
	),
	"users" AS (
		INSERT INTO m_users ("code")
			SELECT DISTINCT ("user_id") FROM master_unique_pre
			ON CONFLICT ("code") DO UPDATE SET "code"=EXCLUDED."code"
			RETURNING *
		),
	"master_prepared" AS (
		SELECT 
			"companies"."id" "company_id",
			"companies"."code" "company_code",
			"offices"."id" "office_id",
			"offices"."code" "office_code",
			"car_numbers"."id" "car_number_id",
			"car_numbers"."code" "car_number_code",
			"users"."id" "user_id",
			"users"."code" "user_code"
		FROM master_unique_pre mup
			INNER JOIN	"companies" ON "companies"."code" = mup."company_id"
			INNER JOIN	"offices" ON "offices"."code" = mup."office_id"
			INNER JOIN	"car_numbers" ON "car_numbers"."code" = mup."car_number"
			INNER JOIN	"users" ON "users"."code" = mup."user_id"
	),
	"drives" AS (
		INSERT INTO t_drive ("company_id", "office_id", "car_number_id", "user_id")
			SELECT 
				"company_id",
				"office_id",
				"car_number_id",
				"user_id"
			FROM master_prepared mup
		ON CONFLICT ON CONSTRAINT t_drive_un DO UPDATE SET 
			"company_id"=EXCLUDED."company_id",
			"office_id"=EXCLUDED."office_id",
			"car_number_id"=EXCLUDED."car_number_id",
			"user_id"=EXCLUDED."user_id"
		RETURNING *
	)
	INSERT INTO t_positions (
		"date",
		"timestamp",
		"drive_id",
		"latitude",
		"longitude",
		"speed",
		"mapped_latitude",
		"mapped_longitude",
		"distance",
		"d_kbn"
		) SELECT
			ts."date" "date",
			ts."timestamp" "timestamp",
			drives.id "drive_id",
			ts.latitude,
			ts.longitude,
			ts.speed,
			ts.mapped_latitude,
			ts.mapped_longitude,
			ts.distance,
			ts.d_kbn
		FROM temp_sensors_map_ ts
		INNER JOIN master_prepared mp ON 
			mp.company_code = ts.company_id
			AND mp.office_code = ts.office_id
			AND mp.car_number_code = ts.car_number
			AND mp.user_code = ts.user_id
		INNER JOIN drives ON
			drives.office_id = mp.office_id
			AND drives.car_number_id = mp.car_number_id
			AND drives.company_id = mp.company_id
			AND drives.user_id = mp.user_id;
	raise INFO '[%] inserted: %', pg_backend_pid(), file_name;
END;
$procedure$;
