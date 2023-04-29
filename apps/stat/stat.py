# %% import
import polars as pl

# %% read csv
dtypes = {
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
csv = pl.read_csv("./data/events/*.csv", dtypes=dtypes, try_parse_dates=False)

# %% count by hour
csv.select(pl.col("timestamp").dt.hour().alias("time_hour")).groupby("time_hour").agg(
    [pl.count()]
).sort("time_hour")

# %%
