#%% import
import polars as pl

# def event_rate_per_hour(df: pl.DataFrame):
#     rows = df.count()
#     print(rows)
#     count_event = df.groupby([df["timestamp"].dt.hour]).event_id.count()
#     print(count_event)
#     return count_event / rows

#%% read csv
csv = pl.read_csv("./data/events/events_20220101.csv")
print(csv)
# print(event_rate_per_hour(csv))
