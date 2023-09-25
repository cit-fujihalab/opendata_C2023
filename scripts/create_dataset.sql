select distinct tv.user_id,
                tm.body_temp,
                tm.spo2,
                tm.sys,
                tm.dia,
                tm.fatigue_level_id,
                tm.fatigue_lh,
                tm.fatigue_deviation,
                tu.sex_id,
                tu.generation_id,
                tc.total_weight,
                tc."length",
                tc."width",
                tc."height",
                case
                    when te.type_id is null then 0
                    else 1
                end
from t_vitals tv
left join t_driving_vitals tdv on tv.user_id = tdv.user_id
left join t_measurements tm on tv.before_measurement_id = tm.id
left join t_events te on tv.user_id = te.user_id
left join t_users tu on tv.user_id = tu.user_id
left join m_car_numbers mcn on tdv.car_number_id = mcn.id
left join temp_cars tc on mcn.code = tc.car_number
where tdv.user_id is not null
    and tm.body_temp is not null
