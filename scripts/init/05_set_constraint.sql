SET work_mem to '16GB';
SET maintenance_work_mem to '8GB';
SET temp_tablespaces='tbsp_z';
ANALYZE VERBOSE;

-- postgres.t_events index
CREATE INDEX t_events_type_id_idx ON postgres.t_events USING btree ("type_id") TABLESPACE tbsp_z;
CREATE INDEX t_events_timestamp_idx ON postgres.t_events USING btree ("timestamp") TABLESPACE tbsp_z;

-- postgres.t_events foreign keys
ALTER TABLE postgres.t_events ADD CONSTRAINT t_events_fk FOREIGN KEY (company_id) REFERENCES postgres.m_companies(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_events ADD CONSTRAINT t_events_fk_1 FOREIGN KEY (office_id) REFERENCES postgres.m_offices(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_events ADD CONSTRAINT t_events_fk_2 FOREIGN KEY (car_number_id) REFERENCES postgres.m_car_numbers(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_events ADD CONSTRAINT t_events_fk_3 FOREIGN KEY (user_id) REFERENCES postgres.m_users(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_events ADD CONSTRAINT t_events_fk_4 FOREIGN KEY (type_id) REFERENCES postgres.m_event_types(id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- postgres.t_positions index
CREATE INDEX t_positions_drive_id_idx ON postgres.t_positions USING btree ("drive_id") TABLESPACE tbsp_z;
CREATE INDEX t_positions_timestamp_idx ON postgres.t_positions USING btree ("timestamp") TABLESPACE tbsp_z;

-- postgres.t_positions foreign keys
ALTER TABLE postgres.t_positions ADD CONSTRAINT t_positions_fk FOREIGN KEY (drive_id) REFERENCES postgres.t_drive(id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- postgres.t_driving_vitals foreign keys
ALTER TABLE postgres.t_driving_vitals ADD CONSTRAINT t_driving_vitals_fk FOREIGN KEY (company_id) REFERENCES postgres.m_companies(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_driving_vitals ADD CONSTRAINT t_driving_vitals_fk_1 FOREIGN KEY (office_id) REFERENCES postgres.m_offices(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_driving_vitals ADD CONSTRAINT t_driving_vitals_fk_2 FOREIGN KEY (car_number_id) REFERENCES postgres.m_car_numbers(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_driving_vitals ADD CONSTRAINT t_driving_vitals_fk_3 FOREIGN KEY (user_id) REFERENCES postgres.m_users(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_driving_vitals ADD CONSTRAINT t_driving_vitals_fk_4 FOREIGN KEY (fatigue_score_id) REFERENCES postgres.m_fatigue_scores(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_driving_vitals ADD CONSTRAINT t_driving_vitals_fk_5 FOREIGN KEY (fatigue_level_id) REFERENCES postgres.m_fatigue_levels(id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- postgres.t_measurements foreign keys
ALTER TABLE postgres.t_measurements ADD CONSTRAINT t_measurements_fk FOREIGN KEY (judge_id) REFERENCES postgres.m_judgements(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_measurements ADD CONSTRAINT t_measurements_fk_1 FOREIGN KEY (fatigue_score_id) REFERENCES postgres.m_fatigue_scores(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_measurements ADD CONSTRAINT t_measurements_fk_2 FOREIGN KEY (fatigue_level_id) REFERENCES postgres.m_fatigue_levels(id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- postgres.t_vitals foreign keys
ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk FOREIGN KEY (company_id) REFERENCES postgres.m_companies(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_1 FOREIGN KEY (office_id) REFERENCES postgres.m_offices(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_2 FOREIGN KEY (user_id) REFERENCES postgres.m_users(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_3 FOREIGN KEY (before_measurement_id) REFERENCES postgres.t_measurements(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_4 FOREIGN KEY (after_measurement_id) REFERENCES postgres.t_measurements(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_5 FOREIGN KEY (before_crew_judge_id) REFERENCES postgres.m_crew_judge_types(id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE postgres.t_vitals ADD CONSTRAINT t_vitals_fk_6 FOREIGN KEY (before_crew_judge_reason_id) REFERENCES postgres.m_crew_judge_reasons(id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- postgres.t_vitals index
CREATE INDEX t_vitals_timestamp_idx ON postgres.t_vitals USING btree ("date") TABLESPACE tbsp_z;
