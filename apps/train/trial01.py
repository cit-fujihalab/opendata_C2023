# %% import
import datetime as dt

import polars as pl
from pycaret.classification import *

EVENTS_USERS_FILE = "./out/event_type_user_2023-05-10 21-13-39.csv"
VITAL_FILE = "./data/vitals/vitals_*.csv"
# POSITIONS_FILE = "./data/sensors_map/sensors_map_"
OUT_DIR = "./out"
# START_DATE = dt.date(2022, 1, 1)
# END_DATE = dt.date(2022, 12, 31)


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

vitals = pl.scan_csv(VITAL_FILE, dtypes=vital_dtypes)

all_user = vitals.select([pl.col("user_id")]).unique("user_id").collect()

# %%
event_user_dtype = {
    "user_id": pl.Utf8,
    "event_id": pl.Utf8,
    "count": pl.Utf8,
}

event_user = (
    pl.read_csv(EVENTS_USERS_FILE, dtypes=event_user_dtype)
    .select([pl.col("user_id")])
    .unique("user_id")
)

# %%
event_user_detail = event_user.join(
    vitals.select(
        [
            pl.col("user_id"),
            # pl.col("before_judge_id"),
            pl.col("before_body_temp"),
            pl.col("before_spo2"),
            pl.col("before_sys"),
            pl.col("before_dia"),
            pl.col("before_fatigue_lh"),
            pl.col("before_fatigue_deviation"),
        ]
    )
    .drop_nulls()
    .collect()
    .with_columns([pl.lit(True).alias("trg")]),
    on=[pl.col("user_id")],
    how="inner",
)

# %%
non_event_user_detail = all_user.filter(
    pl.col("user_id").is_in(event_user.get_column("user_id")).is_not()
).join(
    vitals.select(
        [
            pl.col("user_id"),
            # pl.col("before_judge_id"),
            pl.col("before_body_temp"),
            pl.col("before_spo2"),
            pl.col("before_sys"),
            pl.col("before_dia"),
            pl.col("before_fatigue_lh"),
            pl.col("before_fatigue_deviation"),
        ]
    )
    .drop_nulls()
    .collect()
    .with_columns([pl.lit(False).alias("trg")]),
    on=[pl.col("user_id")],
    how="inner",
)

# %%
x = pl.concat([event_user_detail, non_event_user_detail])

# %%
s = setup(x.to_pandas(), target="trg", ignore_features=["user_id"], session_id=123)

# %%
best = compare_models()

# %%
model = create_model("lr")
# %%
evaluate_model(model)
# %%
