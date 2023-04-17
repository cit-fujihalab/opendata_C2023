call insert_unique('temp1', 'company_id', 'm_company', 'name');
call insert_unique('temp1', 'office_id', 'm_office', 'name');
call insert_unique('temp1', 'user_id', 'm_user', 'name');
call insert_unique('temp1', 'before_judge_name', 'm_judge', 'name');
call insert_unique('temp1', 'after_judge_name', 'm_judge', 'name');
call insert_unique('temp1', 'before_fatigue_score_name', 'm_fatigue_score_name', 'name');
call insert_unique('temp1', 'after_fatigue_score_name', 'm_fatigue_score_name', 'name');
call insert_unique('temp1', 'before_fatigue_level_name', 'm_fatigue_level_name', 'name');
call insert_unique('temp1', 'after_fatigue_level_name', 'm_fatigue_level_name', 'name');
call insert_unique('temp1', 'before_crew_judge_name', 'm_crew_judge', 'name');
call insert_unique('temp1', 'before_crew_judge_reason_name', 'm_crew_judge_reason', 'name');


call insert_unique('temp_events', 'company_id', 'm_companies', 'code');
call insert_unique('temp_events', 'office_id', 'm_offices', 'code');
call insert_unique('temp_events', 'car_number', 'm_car_numbers', 'code');
call insert_unique('temp_events', 'user_id', 'm_users', 'code');
call insert_unique('temp_events', 'event_id', 'm_event_types', 'code');


call insert_unique('temp_sensors_map', 'company_id', 'm_companies', 'code');
call insert_unique('temp_sensors_map', 'office_id', 'm_offices', 'code');
call insert_unique('temp_sensors_map', 'car_number', 'm_car_numbers', 'code');
call insert_unique('temp_sensors_map', 'user_id', 'm_users', 'code');
