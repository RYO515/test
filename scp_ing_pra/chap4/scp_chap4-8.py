import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("FEH_00200524_210121222550.csv", index_col="全国・都道府県", encoding="shift_jis")

# 全国の合計が大きいのでdrop
df = df.drop("全国", axis=0)
# 平成30年のグラフを作成するけど「,」邪魔だから除去
df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",", ""))
# 降順で並び替え
df = df.sort_values("平成30年", ascending=False)
# グラフの画面サイズを指定
df["平成30年"].plot.bar(figsize=(10,6))
plt.show()
