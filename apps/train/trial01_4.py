# %% import
import datetime as dt

import polars as pl
from pycaret.classification import *

EVENTS_USERS_FILE = "./out/event_type_user_2023-05-10 21-13-39.csv"
VITALS_FILE = "./data/vitals/vitals_*.csv"
CARS_FILE = "./data/master_cars_202301.csv"
USERS_FILE = "./data/master_users_202301.csv"
DRIVING_VITALS_FILE = "./data/driving_vitals/driving_vitals_*.csv"
POSITIONS_FILE = "./data/sensors_map/sensors_map_"

OUT_DIR = "./out"

EVENT_ID = "100"


# %% load data
vital_dtypes = {
    "date": pl.Utf8,
    "company_id": pl.Utf8,
    "office_id": pl.Utf8,
    "user_id": pl.Utf8,
    "before_timestamp": pl.Utf8,
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

vitals = pl.scan_csv(VITALS_FILE, dtypes=vital_dtypes)
driving_vitals = pl.scan_csv(DRIVING_VITALS_FILE, dtypes=driving_vital_dtypes)
cars = pl.read_csv(CARS_FILE, dtypes=car_dtypes).select(
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
users = pl.read_csv(USERS_FILE, dtypes=car_dtypes).select(
    [
        pl.col("user_id"),
        pl.col("性別").alias("sex"),
        pl.col("年代").alias("age"),
    ]
)


# %%
user_car = (
    driving_vitals.select(
        [
            pl.col("user_id"),
            pl.col("car_number"),
        ]
    )
    .unique("user_id")
    .collect()
    .join(cars, on="car_number", how="inner")
)

# %%
all_user = vitals.select([pl.col("user_id")]).unique("user_id").collect()

# %%
event_user_dtype = {
    "user_id": pl.Utf8,
    "event_id": pl.Utf8,
    "count": pl.Utf8,
}

event_user = (
    pl.read_csv(EVENTS_USERS_FILE, dtypes=event_user_dtype)
    .filter(pl.col("event_id").is_in([EVENT_ID]))
    .select([pl.col("user_id")])
    .unique("user_id")
    .join(user_car, on="user_id", how="inner")
)

event_user_detail = (
    event_user.join(
        vitals.select(
            [
                pl.col("user_id"),
                pl.col("before_body_temp"),
                pl.col("before_spo2"),
                pl.col("before_sys"),
                pl.col("before_dia"),
                pl.col("before_fatigue_lh"),
                pl.col("before_fatigue_deviation"),
            ]
        ).collect(),
        on=[pl.col("user_id")],
        how="inner",
    )
    .join(users, on="user_id", how="inner")
    .with_columns([pl.lit(True).alias("trg")])
)

# %%
non_event_user = all_user.filter(
    pl.col("user_id").is_in(event_user.get_column("user_id")).is_not()
)

non_event_user_detail = (
    non_event_user.join(user_car, on="user_id", how="inner")
    .join(
        vitals.select(
            [
                pl.col("user_id"),
                pl.col("before_body_temp"),
                pl.col("before_spo2"),
                pl.col("before_sys"),
                pl.col("before_dia"),
                pl.col("before_fatigue_lh"),
                pl.col("before_fatigue_deviation"),
            ]
        ).collect(),
        on=[pl.col("user_id")],
        how="inner",
    )
    .join(users, on="user_id", how="inner")
    .with_columns([pl.lit(False).alias("trg")])
)

# %%
x = pl.concat([event_user_detail, non_event_user_detail])

# %%
s = setup(
    x.to_pandas(),
    target="trg",
    ignore_features=["user_id", "car_number"],
    session_id=123,
)

# %%
best = compare_models()

# %%
model = create_model("ada")

# %%
evaluate_model(model)

# %%
