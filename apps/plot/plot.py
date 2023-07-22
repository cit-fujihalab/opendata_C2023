# %% import
import csv

import matplotlib.pyplot as plt
import polars as pl

event_id_list = []
count_list = []
time_list = []
d = {
    "100": "前方不注意",
    "300": "衝撃",
    "400": "車間距離警報",
    "900": "緊急ボタン押下",
    "800101": "急加速",
    "800102": "急減速",
    "800103": "急ハンドル",
    "800104": "車間距離不足",
    "800105": "脇見",
    "800106": "一時不停止",
    "800107": "速度超過",
    "10000002": "IoTボタン押下",
}

remove_string = "count"

# %% read event csv
event_dtypes = {
    "time_hour": int,
    "event_id": str,
    "count": int,
}
read_plot = pl.read_csv(
    "event_type_rate_2023-05-07_18-28-47.csv",
    dtypes=event_dtypes,
    try_parse_dates=False,
)
# %% plot to matplotlib
# print(read_plot.sort("event_id"))

# %% plot to matplotlib
for i in d:
    s = read_plot.filter(pl.col("event_id") == i)
    s.sort("event_id").write_csv(d[i] + "output.csv")

for i in d:
    with open(d[i] + "output.csv") as f:
        reader = csv.reader(f)
        # csvファイルのデータをループ
        print("読み込みファイル", i)
        for row in reader:
            # A列を配列へ格納
            if remove_string not in row:
                time_list.append(int(row[0]))
                # B列を配列へ格納
                count_list.append(int(row[2]))

            else:
                print("該当データなし")
        print(time_list)
        print(count_list)
        # グラフのタイトル、x軸、y軸のラベルを設定する
        # 棒グラフを描画する
        x = time_list
        y = count_list
        plt.title("event_type_id_is_" + i)
        plt.xlabel("X-axis(time)")
        plt.ylabel("Y-axis(frequence)")
        # プロット
        plt.bar(x, y)
        plt.xticks(x)
        plt.savefig(d[i] + "plt.png")
        time_list.clear()
        count_list.clear()
        plt.clf()
        print(time_list)
        print(count_list)
