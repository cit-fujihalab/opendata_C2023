-- postgres.m_car_number_id_seq definition
-- DROP SEQUENCE postgres.m_car_number_id_seq;

CREATE SEQUENCE postgres.m_car_number_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.m_car_number_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.m_car_number_id_seq TO postgres;

-- postgres.m_companies_id_seq definition
-- DROP SEQUENCE postgres.m_companies_id_seq;

CREATE SEQUENCE postgres.m_companies_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 32767
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.m_companies_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.m_companies_id_seq TO postgres;

-- postgres.m_crew_judge_reasons_id_seq definition
-- DROP SEQUENCE postgres.m_crew_judge_reasons_id_seq;

CREATE SEQUENCE postgres.m_crew_judge_reasons_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 32767
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.m_crew_judge_reasons_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.m_crew_judge_reasons_id_seq TO postgres;

-- postgres.m_crew_judge_types_id_seq definition
-- DROP SEQUENCE postgres.m_crew_judge_types_id_seq;

CREATE SEQUENCE postgres.m_crew_judge_types_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 32767
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.m_crew_judge_types_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.m_crew_judge_types_id_seq TO postgres;

-- postgres.m_event_types_id_seq definition
-- DROP SEQUENCE postgres.m_event_types_id_seq;

CREATE SEQUENCE postgres.m_event_types_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 32767
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.m_event_types_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.m_event_types_id_seq TO postgres;

-- postgres.m_fatigue_levels_id_seq definition
-- DROP SEQUENCE postgres.m_fatigue_levels_id_seq;

CREATE SEQUENCE postgres.m_fatigue_levels_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 32767
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.m_fatigue_levels_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.m_fatigue_levels_id_seq TO postgres;

-- postgres.m_fatigue_scores_id_seq definition
-- DROP SEQUENCE postgres.m_fatigue_scores_id_seq;

CREATE SEQUENCE postgres.m_fatigue_scores_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 32767
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.m_fatigue_scores_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.m_fatigue_scores_id_seq TO postgres;

-- postgres.m_judgements_id_seq definition
-- DROP SEQUENCE postgres.m_judgements_id_seq;

CREATE SEQUENCE postgres.m_judgements_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 32767
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.m_judgements_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.m_judgements_id_seq TO postgres;

-- postgres.m_offices_id_seq definition
-- DROP SEQUENCE postgres.m_offices_id_seq;

CREATE SEQUENCE postgres.m_offices_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 32767
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.m_offices_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.m_offices_id_seq TO postgres;

-- postgres.t_acceralations_id_seq definition
-- DROP SEQUENCE postgres.t_acceralations_id_seq;

CREATE SEQUENCE postgres.t_acceralations_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.t_acceralations_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.t_acceralations_id_seq TO postgres;

-- postgres.t_driving_vitals_id_seq definition
-- DROP SEQUENCE postgres.t_driving_vitals_id_seq;

CREATE SEQUENCE postgres.t_driving_vitals_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.t_driving_vitals_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.t_driving_vitals_id_seq TO postgres;

-- postgres.t_events_id_seq definition
-- DROP SEQUENCE postgres.t_events_id_seq;

CREATE SEQUENCE postgres.t_events_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.t_events_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.t_events_id_seq TO postgres;

-- postgres.t_measurements_id_seq definition
-- DROP SEQUENCE postgres.t_measurements_id_seq;

CREATE SEQUENCE postgres.t_measurements_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.t_measurements_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.t_measurements_id_seq TO postgres;

-- postgres.t_positions_id_seq definition
-- DROP SEQUENCE postgres.t_positions_id_seq;

CREATE SEQUENCE postgres.t_positions_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.t_positions_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.t_positions_id_seq TO postgres;

-- postgres.t_vitals_id_seq definition
-- DROP SEQUENCE postgres.t_vitals_id_seq;

CREATE SEQUENCE postgres.t_vitals_id_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647
START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE postgres.t_vitals_id_seq OWNER TO postgres;

GRANT ALL ON SEQUENCE postgres.t_vitals_id_seq TO postgres;

-- postgres.m_companies definition
-- Drop table
-- DROP TABLE postgres.m_companies;

CREATE TABLE postgres.m_companies (
	id smallserial NOT NULL,
	code varchar(7) NOT NULL,
	CONSTRAINT m_companies_pk PRIMARY KEY (id), CONSTRAINT m_companies_un UNIQUE (code)
);

-- postgres.m_offices definition
-- Drop table
-- DROP TABLE postgres.m_offices;

CREATE TABLE postgres.m_offices (
	id smallserial NOT NULL,
	code varchar(12) NOT NULL,
	CONSTRAINT m_offices_pk PRIMARY KEY (id), CONSTRAINT m_offices_un UNIQUE (code)
);

-- postgres.m_users definition
-- Drop table
-- DROP TABLE postgres.m_users;

CREATE TABLE postgres.m_users (
	id serial NOT NULL ,
	code varchar(30) NOT NULL,
	CONSTRAINT m_users_pk PRIMARY KEY (id), CONSTRAINT m_users_un UNIQUE (code)
);

-- postgres.m_car_numbers definition
-- Drop table
-- DROP TABLE postgres.m_car_numbers;

CREATE TABLE postgres.m_car_numbers (
	id serial NOT NULL,
	code varchar(20) NULL,
	CONSTRAINT m_car_numbers_pk PRIMARY KEY (id), CONSTRAINT m_car_numbers_un UNIQUE (code)
);

-- postgres.m_crew_judge_reasons definition
-- Drop table
-- DROP TABLE postgres.m_crew_judge_reasons;

CREATE TABLE postgres.m_crew_judge_reasons (id smallserial NOT NULL,
	code int2 NULL,
	description varchar(50) NULL,
	CONSTRAINT m_crew_judge_reasons_pk PRIMARY KEY (id), CONSTRAINT m_crew_judge_reasons_un UNIQUE (code)
);

-- postgres.m_fatigue_levels definition
-- Drop table
-- DROP TABLE postgres.m_fatigue_levels;

CREATE TABLE postgres.m_fatigue_levels (
	id smallserial NOT NULL,
	code int2 NULL,
	description varchar(20) NULL,
	CONSTRAINT m_fatigue_levels_pk PRIMARY KEY (id), CONSTRAINT m_fatigue_levels_un UNIQUE (code)
);

-- postgres.m_fatigue_scores definition
-- Drop table
-- DROP TABLE postgres.m_fatigue_scores;

CREATE TABLE postgres.m_fatigue_scores (
	id smallserial NOT NULL,
	code int2 NULL,
	description varchar(30) NULL,
	CONSTRAINT m_fatigue_scores_pk PRIMARY KEY (id), CONSTRAINT m_fatigue_scores_un UNIQUE (code)
);

-- postgres.m_judgements definition
-- Drop table
-- DROP TABLE postgres.m_judgements;

CREATE TABLE postgres.m_judgements (
	id smallserial NOT NULL,
	code int2 NULL,
	description varchar(20) NULL,
	CONSTRAINT m_judgements_pk PRIMARY KEY (id), CONSTRAINT m_judgements_un UNIQUE (code)
);

-- postgres.m_event_types definition
-- Drop table
-- DROP TABLE postgres.m_event_types;

CREATE TABLE postgres.m_event_types (
	id smallserial NOT NULL,
	code varchar(10) NULL,
	description varchar(20) NULL,
	CONSTRAINT m_event_types_pk PRIMARY KEY (id), CONSTRAINT m_event_types_un UNIQUE (code)
);

-- postgres.t_events definition
-- Drop table
-- DROP TABLE postgres.t_events;

CREATE TABLE postgres.t_events(
	id serial4 NOT NULL,
	"date" timestamptz NOT NULL,
	"timestamp" timestamptz NOT NULL,
	company_id int2 NOT NULL,
	office_id int2 NOT NULL,
	car_number_id int4 NOT NULL,
	user_id int4 NOT NULL,
	type_id int2 NOT NULL,
	latitude float8 NOT NULL,
	longitude float8 NOT NULL,
	video_file_name1 varchar(70) NOT NULL,
	video_file_name2 varchar(70) NOT NULL,
	d_kbn int2 NOT NULL,
	CONSTRAINT t_events_pk PRIMARY KEY (id), CONSTRAINT t_events_fk
		FOREIGN KEY (company_id) REFERENCES postgres.m_companies(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_events_fk_1
		FOREIGN KEY (office_id) REFERENCES postgres.m_offices(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_events_fk_2
		FOREIGN KEY (car_number_id) REFERENCES postgres.m_car_numbers(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_events_fk_3
		FOREIGN KEY (user_id) REFERENCES postgres.m_users(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_events_fk_4
		FOREIGN KEY (type_id) REFERENCES postgres.m_event_types(id) ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- postgres.t_acceralations definition
-- Drop table
-- DROP TABLE postgres.t_acceralations;

CREATE TABLE postgres.t_acceralations(
	id serial4 NOT NULL,
	"timestamp" timestamptz NOT NULL,
	car_number_id int4 NOT NULL,
	user_id int4 NOT NULL,
	acc_x float8 NOT NULL,
	acc_y float8 NOT NULL,
	acc_z float8 NOT NULL,
	gyr_x float8 NOT NULL,
	gyr_y float8 NOT NULL,
	gyr_z float8 NOT NULL,
	CONSTRAINT t_acceralations_pk PRIMARY KEY (id), CONSTRAINT t_acceralations_fk
		FOREIGN KEY (car_number_id) REFERENCES postgres.m_car_numbers(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_acceralations_fk_1
		FOREIGN KEY (user_id) REFERENCES postgres.m_users(id) ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- postgres.t_positions definition
-- Drop table
-- DROP TABLE postgres.t_positions;

CREATE TABLE postgres.t_positions(
	id serial4 NOT NULL,
	"date" timestamptz NOT NULL,
	"timestamp" timestamptz NOT NULL,
	company_id int2 NOT NULL,
	office_id int2 NOT NULL,
	car_number_id int4 NOT NULL,
	user_id int4 NOT NULL,
	latitude float8 NOT NULL,
	longitude float8 NOT NULL,
	speed float8 NOT NULL,
	mapped_latitude float8 NOT NULL,
	mapped_longitude float8 NOT NULL,
	distance float8 NOT NULL,
	d_kbn int2 NOT NULL,
	CONSTRAINT t_positions_pk PRIMARY KEY (id, "timestamp"), CONSTRAINT t_positions_fk
		FOREIGN KEY (company_id) REFERENCES postgres.m_companies(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_positions_fk_1
		FOREIGN KEY (office_id) REFERENCES postgres.m_offices(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_positions_fk_2
		FOREIGN KEY (car_number_id) REFERENCES postgres.m_car_numbers(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_positions_fk_3
		FOREIGN KEY (user_id) REFERENCES postgres.m_users(id) ON DELETE RESTRICT ON UPDATE RESTRICT
) PARTITION BY RANGE ("timestamp");

CREATE TABLE t_positions_default PARTITION OF t_positions default;

CREATE TABLE t_positions_20220101 PARTITION OF t_positions FOR VALUES FROM ('2022-01-01') TO ('2022-04-01');
CREATE TABLE t_positions_20220401 PARTITION OF t_positions FOR VALUES FROM ('2022-04-01') TO ('2022-07-01');
CREATE TABLE t_positions_20220701 PARTITION OF t_positions FOR VALUES FROM ('2022-07-01') TO ('2022-10-01');
CREATE TABLE t_positions_20220901 PARTITION OF t_positions FOR VALUES FROM ('2022-10-01') TO ('2023-01-01');

-- postgres.t_driving_vitals definition
-- Drop table
-- DROP TABLE postgres.t_driving_vitals;

CREATE TABLE postgres.t_driving_vitals(
	id serial4 NOT NULL,
	"date" timestamptz NOT NULL,
	company_id int2 NOT NULL,
	office_id int2 NOT NULL,
	car_number_id int4 NOT NULL,
	user_id int4 NOT NULL,
	"timestamp" timestamptz NOT NULL,
	fatigue_score_id int2 NOT NULL,
	fatigue_level_id int2 NOT NULL,
	CONSTRAINT t_driving_vitals_pk PRIMARY KEY (id), CONSTRAINT t_driving_vitals_fk
		FOREIGN KEY (company_id) REFERENCES postgres.m_companies(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_driving_vitals_fk_1
		FOREIGN KEY (office_id) REFERENCES postgres.m_offices(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_driving_vitals_fk_2
		FOREIGN KEY (car_number_id) REFERENCES postgres.m_car_numbers(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_driving_vitals_fk_3
		FOREIGN KEY (user_id) REFERENCES postgres.m_users(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_driving_vitals_fk_4
		FOREIGN KEY (fatigue_score_id) REFERENCES postgres.m_fatigue_scores(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_driving_vitals_fk_5
		FOREIGN KEY (fatigue_level_id) REFERENCES postgres.m_fatigue_levels(id) ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- postgres.m_crew_judge_types definition
-- Drop table
-- DROP TABLE postgres.m_crew_judge_types;

CREATE TABLE postgres.m_crew_judge_types (
	id smallserial NOT NULL,
	code int2 NULL,
	description varchar(10) NULL,
	CONSTRAINT m_crew_judge_types_pk PRIMARY KEY (id),
	CONSTRAINT m_crew_judge_types_un UNIQUE (code)
);

-- postgres.t_vitals definition
-- Drop table
-- DROP TABLE postgres.t_vitals;

CREATE TABLE postgres.t_vitals (
	id serial4 NOT NULL,
	"date" timestamptz NOT NULL,
	company_id int2 NOT NULL,
	office_id int2 NOT NULL,
	user_id int4 NOT NULL,
	before_measurement_id int4 NULL,
	after_measurement_id int4 NULL,
	before_crew_judge_id int2 NULL,
	before_crew_judge_reason_id int2 NULL,
	CONSTRAINT t_vitals_pk PRIMARY KEY (id)
);

-- postgres.t_measurements definition
-- Drop table
-- DROP TABLE postgres.t_measurements;

CREATE TABLE postgres.t_measurements (
	id serial4 NOT NULL,
	"timestamp" timestamptz NOT NULL,
	judge_id int2 NULL,
	body_temp float4 NULL,
	spo2 float4 NULL,
	sys float4 NULL,
	dia float4 NULL,
	fatigue_score_id int2 NULL,
	fatigue_level_id int2 NULL,
	fatigue_lh float4 NULL,
	fatigue_deviation float4 NULL,
	cnt int2 NOT NULL,
	CONSTRAINT t_measurements_pk PRIMARY KEY (id)
);

-- postgres.m_crew_judge_types foreign keys
 -- postgres.t_vitals foreign keys

ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk
FOREIGN KEY (company_id) REFERENCES postgres.m_companies(id) ON
DELETE RESTRICT ON
UPDATE RESTRICT;


ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_2
FOREIGN KEY (office_id) REFERENCES postgres.m_offices(id) ON
DELETE RESTRICT ON
UPDATE RESTRICT;


ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_3
FOREIGN KEY (user_id) REFERENCES postgres.m_users(id) ON
DELETE RESTRICT ON
UPDATE RESTRICT;


ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_4
FOREIGN KEY (before_measurement_id) REFERENCES postgres.t_measurements(id) ON
DELETE CASCADE ON
UPDATE CASCADE;


ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_5
FOREIGN KEY (after_measurement_id) REFERENCES postgres.t_measurements(id) ON
DELETE CASCADE ON
UPDATE CASCADE;


ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_6
FOREIGN KEY (before_crew_judge_id) REFERENCES postgres.m_crew_judge_types(id) ON
DELETE RESTRICT ON
UPDATE RESTRICT;


ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_7
FOREIGN KEY (before_crew_judge_reason_id) REFERENCES postgres.m_crew_judge_reasons(id) ON
DELETE RESTRICT ON
UPDATE RESTRICT;

-- postgres.t_measurements foreign keys
