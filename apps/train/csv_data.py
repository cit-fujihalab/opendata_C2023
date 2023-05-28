import polars as pl

vital_dtypes = {
    "date": pl.Utf8,
    "company_id": pl.Utf8,
    "office_id": pl.Utf8,
    "user_id": pl.Utf8,
    "before_timestamp": pl.Datetime,
    "before_judge_id": pl.Utf8,
    "before_judge_name": pl.Utf8,
    "before_body_temp": pl.Float32,
    "before_spo2": pl.Float32,
    "before_sys": pl.Float32,
    "before_dia": pl.Float32,
    "before_fatigue_score_id": pl.Utf8,
    "before_fatigue_score_name": pl.Utf8,
    "before_fatigue_level_id": pl.Utf8,
    "before_fatigue_level_name": pl.Utf8,
    "before_fatigue_lh": pl.Float32,
    "before_fatigue_deviation": pl.Float32,
    "before_cnt": pl.Utf8,
    "before_crew_judge_id": pl.Utf8,
    "before_crew_judge_name": pl.Utf8,
    "before_crew_judge_reason_id": pl.Utf8,
    "before_crew_judge_reason_name": pl.Utf8,
    "after_timestamp": pl.Utf8,
    "after_judge_id": pl.Utf8,
    "after_judge_name": pl.Utf8,
    "after_body_temp": pl.Utf8,
    "after_spo2": pl.Utf8,
    "after_sys": pl.Utf8,
    "after_dia": pl.Utf8,
    "after_fatigue_score_id": pl.Utf8,
    "after_fatigue_score_name": pl.Utf8,
    "after_fatigue_level_id": pl.Utf8,
    "after_fatigue_level_name": pl.Utf8,
    "after_fatigue_lh": pl.Utf8,
    "after_fatigue_deviation": pl.Utf8,
    "after_cnt": pl.Utf8,
}

driving_vital_dtypes = {
    "date": pl.Utf8,
    "company_id": pl.Utf8,
    "office_id": pl.Utf8,
    "car_number": pl.Utf8,
    "user_id": pl.Utf8,
    "timestamp": pl.Utf8,
    "fatigue_score_id": pl.Utf8,
    "fatigue_score_name": pl.Utf8,
    "fatigue_level_id": pl.Utf8,
    "fatigue_level_name": pl.Utf8,
}

car_dtypes = {
    "car_number": pl.Utf8,
    "車種名称": pl.Utf8,
    "用途": pl.Utf8,
    "最大積載量kg": pl.Int32,
    "車両重量kg": pl.Int32,
    "車両総重量kg": pl.Int32,
    "全長cm": pl.Int16,
    "全幅cm": pl.Int16,
    "全高cm": pl.Int16,
    "排気量ℓ": pl.Float32,
}

positions_dtypes = {
    "date": str,
    "company_id": str,
    "office_id": str,
    "car_number": str,
    "user_id": str,
    "timestamp": pl.Datetime,
    "latitude": float,
    "longitude": float,
    "speed": float,
    "mapped_latitude": float,
    "mapped_longitude": float,
    "distance": float,
    "d_kbn": int,
}

user_dtypes = {
    "user_id": pl.Utf8,
    "性別": pl.Utf8,
    "年代": pl.Utf8,
}

event_user_dtype = {
    "user_id": pl.Utf8,
    "event_id": pl.Utf8,
    "count": pl.Utf8,
}


class DataSet:
    def __init__(
        self,
        vital_file: str,
        driving_vital_file: str,
        car_file: str,
        user_file: str,
        event_user_file: str,
    ) -> None:
        self.vitals = pl.scan_csv(vital_file, dtypes=vital_dtypes)

        self.driving_vitals = pl.scan_csv(
            driving_vital_file, dtypes=driving_vital_dtypes
        )

        self.cars = pl.scan_csv(car_file, dtypes=car_dtypes).select(
            [
                pl.col("car_number"),
                pl.col("最大積載量kg").alias("max_load"),
                pl.col("車両重量kg").alias("car_load"),
                pl.col("車両総重量kg").alias("load"),
                pl.col("全長cm").alias("depth"),
                pl.col("全幅cm").alias("width"),
                pl.col("全高cm").alias("height"),
                pl.col("排気量ℓ").alias("ventilation"),
            ]
        )
        self.users = pl.scan_csv(user_file, dtypes=car_dtypes).select(
            [
                pl.col("user_id"),
                pl.col("性別").alias("sex"),
                pl.col("年代").alias("age"),
            ]
        )

        self.event_users = pl.scan_csv(event_user_file, dtypes=event_user_dtype)
