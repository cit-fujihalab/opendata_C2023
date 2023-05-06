# %% import
import datetime as dt

import polars as pl

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
events = pl.read_csv("./data/events/*.csv", dtypes=event_dtypes, try_parse_dates=False)

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
        "./data/sensors_map/sensors_map_" + date.strftime("%Y%m%d") + ".csv",
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


date = dt.date(2022, 1, 1)
df = count_by_hour(date)
while True:
    date = date + dt.timedelta(days=1)
    if date > dt.date(2022, 12, 31):
        break

    if date.day % 10 == 0:
        print(date)

    try:
        df = pl.concat([df, count_by_hour(date)])
    except:
        pass


# %%
positions_hour = df.groupby("time_hour").agg([pl.col("count").sum()]).sort("time_hour")

# %%
events_hour = (
    events.select(pl.col("timestamp").dt.hour().alias("time_hour"))
    .groupby("time_hour")
    .agg([pl.count()])
    .sort("time_hour")
)

# %%
events_rate_per_hour = events_hour["count"] / events_hour.sum(axis=0)["count"]
positions_rate_per_hour = (
    positions_hour["count"] / positions_hour["count"].cast(dtype=pl.UInt64).sum()
)
# %%
pl.DataFrame(
    [
        events_hour["time_hour"],
        events_hour["count"].alias("events_count"),
        events_rate_per_hour.alias("events_rate"),
        positions_hour["count"].alias("pos_count"),
        positions_rate_per_hour.alias("positions_rate"),
        (events_rate_per_hour / positions_rate_per_hour).alias("rel_events_rate"),
    ],
)


# %%
