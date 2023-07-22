CREATE SCHEMA postgres;
CREATE TABLESPACE tbsp_e LOCATION '/var/mnt/sde';
CREATE TABLESPACE tbsp_o LOCATION '/var/mnt/sdo';
CREATE TABLESPACE tbsp_p LOCATION '/var/mnt/sdp';
CREATE TABLESPACE tbsp_q LOCATION '/var/mnt/sdq';
CREATE TABLESPACE tbsp_z LOCATION '/var/mnt/sdz';

ALTER TABLESPACE tbsp_z SET (random_page_cost=1.1);
ALTER TABLESPACE tbsp_z SET (effective_io_concurrency=20);

CREATE TABLE postgres.m_car_numbers (
	id serial NOT NULL,
	code varchar(20) NOT NULL,
	CONSTRAINT m_car_numbers_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_car_numbers_un UNIQUE (code) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.m_companies (
	id smallserial NOT NULL,
	code varchar(7) NOT NULL,
	CONSTRAINT m_companies_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_companies_un UNIQUE (code) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.m_crew_judge_reasons (
	id smallserial NOT NULL,
	code varchar(4) NOT NULL,
	description varchar(50) NULL,
	CONSTRAINT m_crew_judge_reasons_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_crew_judge_reasons_un UNIQUE (code) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.m_crew_judge_types (
	id smallserial NOT NULL,
	code varchar(4) NOT NULL,
	description varchar(10) NULL,
	CONSTRAINT m_crew_judge_types_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_crew_judge_types_un UNIQUE (code) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.m_event_types (
	id smallserial NOT NULL,
	code varchar(10) NOT NULL,
	description varchar(20) NULL,
	CONSTRAINT m_event_types_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_event_types_un UNIQUE (code) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.m_fatigue_levels (
	id smallserial NOT NULL,
	code varchar(4) NULL,
	description varchar(20) NULL,
	CONSTRAINT m_fatigue_levels_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_fatigue_levels_un UNIQUE (description) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.m_fatigue_scores (
	id smallserial NOT NULL,
	code varchar(4) NULL,
	description varchar(30) NULL,
	CONSTRAINT m_fatigue_scores_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_fatigue_scores_un UNIQUE (description) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.m_judgements (
	id smallserial NOT NULL,
	code varchar(4) NOT NULL,
	description varchar(20) NULL,
	CONSTRAINT m_judgements_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_judgements_un UNIQUE (code) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.m_offices (
	id smallserial NOT NULL,
	code varchar(12) NOT NULL,
	CONSTRAINT m_offices_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_offices_un UNIQUE (code) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.m_users (
	id serial NOT NULL ,
	code varchar(30) NOT NULL,
	CONSTRAINT m_users_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z,
	CONSTRAINT m_users_un UNIQUE (code) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_z;

CREATE TABLE postgres.t_events(
	id serial4 NOT NULL,
	"date" varchar(8) NOT NULL,
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
	CONSTRAINT t_events_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_o;

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
) TABLESPACE tbsp_o;

CREATE TABLE postgres.t_positions (
	"date" varchar(8) NOT NULL,
	"timestamp" timestamptz NOT NULL,
	company_id int2 NOT NULL,
	office_id int2 NOT NULL,
	car_number_id int4 NOT NULL,
	user_id int4 NOT NULL,
	latitude float8 NOT NULL,
	longitude float8 NOT NULL,
	speed float4 NOT NULL,
	mapped_latitude float8 NOT NULL,
	mapped_longitude float8 NOT NULL,
	distance float8 NOT NULL,
	d_kbn varchar(1) NOT NULL
)
PARTITION BY LIST (date);

CREATE TABLE t_positions_default PARTITION OF t_positions default;

CREATE TABLE t_positions_20220101 PARTITION OF t_positions FOR VALUES IN (
	'20220101', '20220102', '20220103', '20220104', '20220105', 
	'20220106', '20220107', '20220108', '20220109', '20220110') TABLESPACE tbsp_o;
CREATE TABLE t_positions_20220111 PARTITION OF t_positions FOR VALUES IN (
	'20220111', '20220112', '20220113', '20220114', '20220115', 
	'20220116', '20220117', '20220118', '20220119', '20220120') TABLESPACE tbsp_o;
CREATE TABLE t_positions_20220121 PARTITION OF t_positions FOR VALUES IN (
	'20220121', '20220122', '20220123', '20220124', '20220125', 
	'20220126', '20220127', '20220128', '20220129', '20220130', '20220131') TABLESPACE tbsp_o;

CREATE TABLE t_positions_20220201 PARTITION OF t_positions FOR VALUES IN (
	'20220201', '20220202', '20220203', '20220204', '20220205', 
	'20220206', '20220207', '20220208', '20220209', '20220210') TABLESPACE tbsp_o;
CREATE TABLE t_positions_20220211 PARTITION OF t_positions FOR VALUES IN (
	'20220211', '20220212', '20220213', '20220214', '20220215', 
	'20220216', '20220217', '20220218', '20220219', '20220220') TABLESPACE tbsp_o;
CREATE TABLE t_positions_20220221 PARTITION OF t_positions FOR VALUES IN (
	'20220221', '20220222', '20220223', '20220224', '20220225', 
	'20220226', '20220227', '20220228') TABLESPACE tbsp_o;

CREATE TABLE t_positions_20220301 PARTITION OF t_positions FOR VALUES IN (
	'20220301', '20220302', '20220303', '20220304', '20220305', 
	'20220306', '20220307', '20220308', '20220309', '20220310') TABLESPACE tbsp_o;
CREATE TABLE t_positions_20220311 PARTITION OF t_positions FOR VALUES IN (
	'20220311', '20220312', '20220313', '20220314', '20220315', 
	'20220316', '20220317', '20220318', '20220319', '20220320') TABLESPACE tbsp_o;
CREATE TABLE t_positions_20220321 PARTITION OF t_positions FOR VALUES IN (
	'20220321', '20220322', '20220323', '20220324', '20220325', 
	'20220326', '20220327', '20220328', '20220329', '20220330', '20220331') TABLESPACE tbsp_o;

CREATE TABLE t_positions_20220401 PARTITION OF t_positions FOR VALUES IN (
	'20220401', '20220402', '20220403', '20220404', '20220405', 
	'20220406', '20220407', '20220408', '20220409', '20220410') TABLESPACE tbsp_o;
CREATE TABLE t_positions_20220411 PARTITION OF t_positions FOR VALUES IN (
	'20220411', '20220412', '20220413', '20220414', '20220415', 
	'20220416', '20220417', '20220418', '20220419', '20220420') TABLESPACE tbsp_o;
CREATE TABLE t_positions_20220421 PARTITION OF t_positions FOR VALUES IN (
	'20220421', '20220422', '20220423', '20220424', '20220425', 
	'20220426', '20220427', '20220428', '20220429', '20220430') TABLESPACE tbsp_o;

CREATE TABLE t_positions_20220501 PARTITION OF t_positions FOR VALUES IN (
	'20220501', '20220502', '20220503', '20220504', '20220505', 
	'20220506', '20220507', '20220508', '20220509', '20220510') TABLESPACE tbsp_p;
CREATE TABLE t_positions_20220511 PARTITION OF t_positions FOR VALUES IN (
	'20220511', '20220512', '20220513', '20220514', '20220515', 
	'20220516', '20220517', '20220518', '20220519', '20220520') TABLESPACE tbsp_p;
CREATE TABLE t_positions_20220521 PARTITION OF t_positions FOR VALUES IN (
	'20220521', '20220522', '20220523', '20220524', '20220525', 
	'20220526', '20220527', '20220528', '20220529', '20220530', '20220531') TABLESPACE tbsp_p;

CREATE TABLE t_positions_20220601 PARTITION OF t_positions FOR VALUES IN (
	'20220601', '20220602', '20220603', '20220604', '20220605', 
	'20220606', '20220607', '20220608', '20220609', '20220610') TABLESPACE tbsp_p;
CREATE TABLE t_positions_20220611 PARTITION OF t_positions FOR VALUES IN (
	'20220611', '20220612', '20220613', '20220614', '20220615', 
	'20220616', '20220617', '20220618', '20220619', '20220620') TABLESPACE tbsp_p;
CREATE TABLE t_positions_20220621 PARTITION OF t_positions FOR VALUES IN (
	'20220621', '20220622', '20220623', '20220624', '20220625', 
	'20220626', '20220627', '20220628', '20220629', '20220630') TABLESPACE tbsp_p;

CREATE TABLE t_positions_20220701 PARTITION OF t_positions FOR VALUES IN (
	'20220701', '20220702', '20220703', '20220704', '20220705', 
	'20220706', '20220707', '20220708', '20220709', '20220710') TABLESPACE tbsp_p;
CREATE TABLE t_positions_20220711 PARTITION OF t_positions FOR VALUES IN (
	'20220711', '20220712', '20220713', '20220714', '20220715', 
	'20220716', '20220717', '20220718', '20220719', '20220720') TABLESPACE tbsp_p;
CREATE TABLE t_positions_20220721 PARTITION OF t_positions FOR VALUES IN (
	'20220721', '20220722', '20220723', '20220724', '20220725', 
	'20220726', '20220727', '20220728', '20220729', '20220730', '20220731') TABLESPACE tbsp_p;

CREATE TABLE t_positions_20220801 PARTITION OF t_positions FOR VALUES IN (
	'20220801', '20220802', '20220803', '20220804', '20220805', 
	'20220806', '20220807', '20220808', '20220809', '20220810') TABLESPACE tbsp_p;
CREATE TABLE t_positions_20220811 PARTITION OF t_positions FOR VALUES IN (
	'20220811', '20220812', '20220813', '20220814', '20220815', 
	'20220816', '20220817', '20220818', '20220819', '20220820') TABLESPACE tbsp_p;
CREATE TABLE t_positions_20220821 PARTITION OF t_positions FOR VALUES IN (
	'20220821', '20220822', '20220823', '20220824', '20220825', 
	'20220826', '20220827', '20220828', '20220829', '20220830', '20220831') TABLESPACE tbsp_p;

CREATE TABLE t_positions_20220901 PARTITION OF t_positions FOR VALUES IN (
	'20220901', '20220902', '20220903', '20220904', '20220905', 
	'20220906', '20220907', '20220908', '20220909', '20220910') TABLESPACE tbsp_q;
CREATE TABLE t_positions_20220911 PARTITION OF t_positions FOR VALUES IN (
	'20220911', '20220912', '20220913', '20220914', '20220915', 
	'20220916', '20220917', '20220918', '20220919', '20220920') TABLESPACE tbsp_q;
CREATE TABLE t_positions_20220921 PARTITION OF t_positions FOR VALUES IN (
	'20220921', '20220922', '20220923', '20220924', '20220925', 
	'20220926', '20220927', '20220928', '20220929', '20220930') TABLESPACE tbsp_q;

CREATE TABLE t_positions_20221001 PARTITION OF t_positions FOR VALUES IN (
	'20221001', '20221002', '20221003', '20221004', '20221005', 
	'20221006', '20221007', '20221008', '20221009', '20221010') TABLESPACE tbsp_q;
CREATE TABLE t_positions_20221011 PARTITION OF t_positions FOR VALUES IN (
	'20221011', '20221012', '20221013', '20221014', '20221015', 
	'20221016', '20221017', '20221018', '20221019', '20221020') TABLESPACE tbsp_q;
CREATE TABLE t_positions_20221021 PARTITION OF t_positions FOR VALUES IN (
	'20221021', '20221022', '20221023', '20221024', '20221025', 
	'20221026', '20221027', '20221028', '20221029', '20221030', '20221031') TABLESPACE tbsp_q;

CREATE TABLE t_positions_20221101 PARTITION OF t_positions FOR VALUES IN (
	'20221101', '20221102', '20221103', '20221104', '20221105', 
	'20221106', '20221107', '20221108', '20221109', '20221110') TABLESPACE tbsp_q;
CREATE TABLE t_positions_20221111 PARTITION OF t_positions FOR VALUES IN (
	'20221111', '20221112', '20221113', '20221114', '20221115', 
	'20221116', '20221117', '20221118', '20221119', '20221120') TABLESPACE tbsp_q;
CREATE TABLE t_positions_20221121 PARTITION OF t_positions FOR VALUES IN (
	'20221121', '20221122', '20221123', '20221124', '20221125', 
	'20221126', '20221127', '20221128', '20221129', '20221130') TABLESPACE tbsp_q;

CREATE TABLE t_positions_20221201 PARTITION OF t_positions FOR VALUES IN (
	'20221201', '20221202', '20221203', '20221204', '20221205', 
	'20221206', '20221207', '20221208', '20221209', '20221210') TABLESPACE tbsp_q;
CREATE TABLE t_positions_20221211 PARTITION OF t_positions FOR VALUES IN (
	'20221211', '20221212', '20221213', '20221214', '20221215', 
	'20221216', '20221217', '20221218', '20221219', '20221220') TABLESPACE tbsp_q;
CREATE TABLE t_positions_20221221 PARTITION OF t_positions FOR VALUES IN (
	'20221221', '20221222', '20221223', '20221224', '20221225', 
	'20221226', '20221227', '20221228', '20221229', '20221230', '20221231') TABLESPACE tbsp_q;

CREATE TABLE postgres.t_driving_vitals(
	id serial4 NOT NULL,
	"date" VARCHAR(8) NOT NULL,
	"timestamp" timestamptz NOT NULL,
	company_id int2 NOT NULL,
	office_id int2 NOT NULL,
	car_number_id int4 NOT NULL,
	user_id int4 NOT NULL,
	fatigue_score_id int2 NULL,
	fatigue_level_id int2 NULL,
	CONSTRAINT t_driving_vitals_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_o;

CREATE TABLE postgres.t_measurements (
	id serial8 NOT NULL,
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
	CONSTRAINT t_measurements_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_q;

CREATE TABLE postgres.t_vitals (
	id serial8 NOT NULL,
	"date" varchar(8) NOT NULL,
	company_id int2 NOT NULL,
	office_id int2 NOT NULL,
	user_id int4 NOT NULL,
	before_measurement_id int4 NULL,
	after_measurement_id int4 NULL,
	before_crew_judge_id int2 NULL,
	before_crew_judge_reason_id int2 NULL,
	CONSTRAINT t_vitals_pk PRIMARY KEY (id) USING INDEX TABLESPACE tbsp_z
) TABLESPACE tbsp_q;
