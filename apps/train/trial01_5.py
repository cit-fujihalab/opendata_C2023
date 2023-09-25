# %% import
import polars as pl
from csv_data import DataSet
from pycaret.classification import (
    create_model,
    evaluate_model,
    finalize_model,
    save_model,
    setup,
    tune_model,
)

EVENTS_USERS_FILE = "./out/event_type_user_2023-05-10 21-13-39.csv"
VITALS_FILE = "./data/vitals/vitals_*.csv"
CARS_FILE = "./data/master_cars_202301.csv"
EVENTS_FILE = "./data/events/events_*.csv"
USERS_FILE = "./data/master_users_202301.csv"
DRIVING_VITALS_FILE = "./data/driving_vitals/driving_vitals_*.csv"
POSITIONS_FILE = "./data/sensors_map/sensors_map_"

EVENT_ID = "800102"


# %%
ds = DataSet(
    vital_file=VITALS_FILE,
    driving_vital_file=DRIVING_VITALS_FILE,
    car_file=CARS_FILE,
    event_file=EVENTS_FILE,
    user_file=USERS_FILE,
    event_user_file=EVENTS_USERS_FILE,
)

# %% Target features
event_user = (
    ds.event_users.filter(pl.col("event_id").is_in([EVENT_ID]))
    .select([pl.col("user_id")])
    .unique("user_id")
    .with_columns([pl.lit(True).alias("trg")])
    .collect()
)

non_event_user = (
    ds.vitals.filter(pl.col("user_id").is_in(event_user.get_column("user_id")).is_not())
    .select([pl.col("user_id")])
    .unique("user_id")
    .with_columns([pl.lit(False).alias("trg")])
    .collect()
)

# %% Car features
car_features = [
    pl.col("car_number"),
    pl.col("max_load"),
    pl.col("car_load"),
    pl.col("load"),
    pl.col("depth"),
    pl.col("width"),
    pl.col("height"),
    pl.col("ventilation"),
]

user_car = (
    pl.concat(
        [
            ds.driving_vitals.select(
                [
                    pl.col("user_id"),
                    pl.col("car_number"),
                ]
            ),
            ds.events.select(
                [
                    pl.col("user_id"),
                    pl.col("car_number"),
                ]
            ),
        ]
    )
    .unique("user_id")
    .collect()
    .join(
        ds.cars.select(car_features).collect(),
        on="car_number",
        how="inner",
    )
)

# %% User features
user_features = [
    pl.col("user_id"),
    pl.col("sex"),
    pl.col("age"),
]

users = ds.users.select(user_features).collect()

# %% Vital features
vital_features = [
    pl.col("user_id"),
    pl.col("before_timestamp").dt.hour().alias("time_hour"),
    pl.col("before_body_temp").alias("body_temp"),
    pl.col("before_spo2").alias("spo2"),
    pl.col("before_sys").alias("sys"),
    pl.col("before_dia").alias("dia"),
    pl.col("before_fatigue_lh").alias("fatigue_lh"),
    pl.col("before_fatigue_deviation").alias("fatigue_deviation"),
]

vitals = ds.vitals.drop_nulls("before_timestamp").select(vital_features).collect()


# %% Concat dataset
def join_features(df_user: pl.DataFrame):
    return (
        df_user.join(vitals, on="user_id", how="inner")
        .join(user_car, on="user_id", how="inner")
        .join(users, on="user_id", how="left")
    )


event_user_detail = join_features(event_user)
non_event_user_detail = join_features(non_event_user)

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
# best = compare_models()

# %%
model = create_model("lr")

# %%
model = tune_model(model)
evaluate_model(model)

# %%
save_model(finalize_model(model), "./models/save_test")

# %%
