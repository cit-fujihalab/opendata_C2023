-- postgres.m_company definition

-- Drop table

-- DROP TABLE postgres.m_company;

CREATE TABLE postgres.m_company (
	id serial4 NOT NULL,
	"name" varchar(50) NOT NULL,
	CONSTRAINT m_company_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE postgres.m_company OWNER TO postgres;
GRANT ALL ON TABLE postgres.m_company TO postgres;


-- postgres.m_crew_judge definition

-- Drop table

-- DROP TABLE postgres.m_crew_judge;

CREATE TABLE postgres.m_crew_judge (
	id serial4 NOT NULL,
	"name" varchar(50) NOT NULL,
	CONSTRAINT m_crew_judge_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE postgres.m_crew_judge OWNER TO postgres;
GRANT ALL ON TABLE postgres.m_crew_judge TO postgres;


-- postgres.m_crew_judge_reason definition

-- Drop table

-- DROP TABLE postgres.m_crew_judge_reason;

CREATE TABLE postgres.m_crew_judge_reason (
	id serial4 NOT NULL,
	"name" varchar(50) NOT NULL,
	CONSTRAINT m_crew_judge_reason_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE postgres.m_crew_judge_reason OWNER TO postgres;
GRANT ALL ON TABLE postgres.m_crew_judge_reason TO postgres;


-- postgres.m_fatigue_level definition

-- Drop table

-- DROP TABLE postgres.m_fatigue_level;

CREATE TABLE postgres.m_fatigue_level (
	id serial4 NOT NULL,
	"name" varchar(50) NOT NULL,
	CONSTRAINT m_fatigue_level_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE postgres.m_fatigue_level OWNER TO postgres;
GRANT ALL ON TABLE postgres.m_fatigue_level TO postgres;


-- postgres.m_fatigue_score definition

-- Drop table

-- DROP TABLE postgres.m_fatigue_score;

CREATE TABLE postgres.m_fatigue_score (
	id serial4 NOT NULL,
	"name" varchar(50) NOT NULL,
	CONSTRAINT m_fatigue_score_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE postgres.m_fatigue_score OWNER TO postgres;
GRANT ALL ON TABLE postgres.m_fatigue_score TO postgres;


-- postgres.m_judge definition

-- Drop table

-- DROP TABLE postgres.m_judge;

CREATE TABLE postgres.m_judge (
	id serial4 NOT NULL,
	"name" varchar(50) NOT NULL,
	CONSTRAINT m_judge_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE postgres.m_judge OWNER TO postgres;
GRANT ALL ON TABLE postgres.m_judge TO postgres;


-- postgres.m_office definition

-- Drop table

-- DROP TABLE postgres.m_office;

CREATE TABLE postgres.m_office (
	id serial4 NOT NULL,
	"name" varchar(50) NULL,
	CONSTRAINT m_office_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE postgres.m_office OWNER TO postgres;
GRANT ALL ON TABLE postgres.m_office TO postgres;


-- postgres.m_user definition

-- Drop table

-- DROP TABLE postgres.m_user;

CREATE TABLE postgres.m_user (
	id serial4 NOT NULL,
	"name" varchar(50) NULL,
	CONSTRAINT m_user_pk PRIMARY KEY (id),
	CONSTRAINT m_user_un UNIQUE (name)
);

-- Permissions

ALTER TABLE postgres.m_user OWNER TO postgres;
GRANT ALL ON TABLE postgres.m_user TO postgres;


-- postgres.t_measure definition

-- Drop table

-- DROP TABLE postgres.t_measure;

CREATE TABLE postgres.t_measure (
	id bigserial NOT NULL,
	"timestamp" timestamptz(0) NOT NULL,
	judge_id int4 NOT NULL,
	body_temp float4 NULL,
	spo2 float4 NULL,
	sys float4 NULL,
	dia float4 NULL,
	fatigue_score_id int4 NULL,
	fatigue_level_id int4 NULL,
	fatigue_lh float4 NULL,
	fatigue_deviation float4 NULL,
	cnt int4 NOT NULL,
	CONSTRAINT t_measure_pk PRIMARY KEY (id),
	CONSTRAINT t_measure_fk FOREIGN KEY (judge_id) REFERENCES postgres.m_judge(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_measure_fk_2 FOREIGN KEY (fatigue_score_id) REFERENCES postgres.m_fatigue_score(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_measure_fk_3 FOREIGN KEY (fatigue_level_id) REFERENCES postgres.m_fatigue_level(id) ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- Permissions

ALTER TABLE postgres.t_measure OWNER TO postgres;
GRANT ALL ON TABLE postgres.t_measure TO postgres;


-- postgres.t_vitals definition

-- Drop table

-- DROP TABLE postgres.t_vitals;

CREATE TABLE postgres.t_vitals (
	id int4 NOT NULL DEFAULT nextval('vitals_id_seq'::regclass),
	company_id int4 NULL,
	office_id int4 NOT NULL,
	user_id int4 NOT NULL,
	before_measure_id int4 NULL,
	after_measure_id int4 NULL,
	before_crew_judge_id int4 NULL,
	before_crew_judge_reason_id int4 NULL,
	CONSTRAINT vitals_pk PRIMARY KEY (id),
	CONSTRAINT t_vitals_fk_1 FOREIGN KEY (before_measure_id) REFERENCES postgres.t_measure(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_vitals_fk_2 FOREIGN KEY (after_measure_id) REFERENCES postgres.t_measure(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_vitals_fk_3 FOREIGN KEY (before_crew_judge_id) REFERENCES postgres.m_crew_judge(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_vitals_fk_4 FOREIGN KEY (before_crew_judge_reason_id) REFERENCES postgres.m_crew_judge_reason(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_vitals_fk_5 FOREIGN KEY (company_id) REFERENCES postgres.m_company(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT t_vitals_fk_6 FOREIGN KEY (office_id) REFERENCES postgres.m_office(id) ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- Permissions

ALTER TABLE postgres.t_vitals OWNER TO postgres;
GRANT ALL ON TABLE postgres.t_vitals TO postgres;
