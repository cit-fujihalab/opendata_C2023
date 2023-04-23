-- vitals
call insert_unique('temp_vitals', 'company_id', 'm_companies', 'code');
call insert_unique('temp_vitals', 'office_id', 'm_offices', 'code');
call insert_unique('temp_vitals', 'user_id', 'm_users', 'code');
call insert_unique('temp_vitals', 'before_judge_name', 'm_judgements', 'description');
call insert_unique('temp_vitals', 'after_judge_name', 'm_judgements', 'description');
call insert_unique('temp_vitals', 'before_fatigue_score_name', 'm_fatigue_scores', 'description');
call insert_unique('temp_vitals', 'after_fatigue_score_name', 'm_fatigue_scores', 'description');
call insert_unique('temp_vitals', 'before_fatigue_level_name', 'm_fatigue_levels', 'description');
call insert_unique('temp_vitals', 'after_fatigue_level_name', 'm_fatigue_levels', 'description');
call insert_unique('temp_vitals', 'before_crew_judge_name', 'm_crew_judge_types', 'description');
call insert_unique('temp_vitals', 'before_crew_judge_reason_name', 'm_crew_judge_reasons', 'description');


call insert_unique('temp_events', 'company_id', 'm_companies', 'code');
call insert_unique('temp_events', 'office_id', 'm_offices', 'code');
call insert_unique('temp_events', 'car_number', 'm_car_numbers', 'code');
call insert_unique('temp_events', 'user_id', 'm_users', 'code');
call insert_unique('temp_events', 'event_id', 'm_event_types', 'code');


call insert_unique('temp_sensors_map', 'company_id', 'm_companies', 'code');
call insert_unique('temp_sensors_map', 'office_id', 'm_offices', 'code');
call insert_unique('temp_sensors_map', 'car_number', 'm_car_numbers', 'code');
call insert_unique('temp_sensors_map', 'user_id', 'm_users', 'code');
