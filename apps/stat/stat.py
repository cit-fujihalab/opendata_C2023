# %% import
import datetime as dt
import json

import polars as pl

EVENTS_FILE = "./data/events/*.csv"
POSITIONS_FILE = "./data/sensors_map/sensors_map_"
OUT_DIR = "out"
START_DATE = dt.date(2022, 1, 1)
END_DATE = dt.date(2022, 12, 31)

# %% read event csv
event_dtypes = {
    "date": str,
    "company_id": str,
    "office_id": str,
    "car_number": str,
    "user_id": str,
    "timestamp": pl.Datetime,
    "event_id": str,
    "event_name": str,
    "latitude": float,
    "longitude": float,
    "d_kbn": int,
    "videofilename1": str,
    "videofilename2": str,
}
events = pl.read_csv(EVENTS_FILE, dtypes=event_dtypes, try_parse_dates=False)

# %% read sensors_map csv
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


# %%
def count_by_hour(date: dt.date):
    pos_csv = pl.scan_csv(
        POSITIONS_FILE + date.strftime("%Y%m%d") + ".csv",
        dtypes=positions_dtypes,
        try_parse_dates=False,
    )
    return (
        pos_csv.select(pl.col("timestamp").dt.hour().alias("time_hour"))
        .groupby("time_hour")
        .agg([pl.count()])
        .sort("time_hour")
        .collect()
    )


# %%
date = START_DATE
df = count_by_hour(date)
while True:
    date = date + dt.timedelta(days=1)
    if date > END_DATE:
        break

    if date.day % 10 == 0:
        print(date)

    try:
        df = pl.concat([df, count_by_hour(date)])
    except:
        pass


# %%
positions_hour = df.groupby("time_hour").agg([pl.col("count").sum()]).sort("time_hour")

events_hour = (
    events.select(pl.col("timestamp").dt.hour().alias("time_hour"))
    .groupby("time_hour")
    .agg([pl.count()])
    .sort("time_hour")
)

events_type_hour = (
    events.select(
        [pl.col("timestamp").dt.hour().alias("time_hour"), pl.col("event_id")]
    )
    .groupby(["time_hour", "event_id"])
    .agg([pl.count()])
    .sort(["time_hour", "event_id"])
)

# %%
event_rate_per_hour = events_hour["count"] / events_hour.sum(axis=0)["count"]
position_rate_per_hour = (
    positions_hour["count"] / positions_hour["count"].cast(dtype=pl.UInt64).sum()
)
# %%
timestamp = dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
pl.DataFrame(
    [
        events_hour["time_hour"].alias("hour"),
        events_hour["count"].alias("events_count"),
        event_rate_per_hour.alias("event_rate"),
        positions_hour["count"].alias("position_count"),
        position_rate_per_hour.alias("position_rate"),
        (event_rate_per_hour / position_rate_per_hour).alias(
            "event_rate / position_rate"
        ),
    ],
).write_csv(OUT_DIR + "/event_rate_" + timestamp + ".csv")

events_type_hour.write_csv(OUT_DIR + "/event_type_rate_" + timestamp + ".csv")

with open(OUT_DIR + "/" + timestamp + ".json", "w") as f:
    json.dump(
        {
            "EVENTS_FILE": EVENTS_FILE,
            "POSITIONS_FILE": POSITIONS_FILE,
            "START_DATE": START_DATE.strftime("%Y%m%d"),
            "END_DATE": END_DATE.strftime("%Y%m%d"),
        },
        f,
        indent=2,
    )


# %%
