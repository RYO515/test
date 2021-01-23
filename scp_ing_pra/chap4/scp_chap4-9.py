import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# df = pd.read_csv("FEH_00200524_210121222550.csv", index_col="全国・都道府県", encoding="shift_jis")
df = pd.read_csv("../../mypackage/FEH_00200524_210121222550.csv", index_col="全国・都道府県", encoding="shift_jis")

df = df.drop("全国", axis=0)
df["平成29年"] = pd.to_numeric(df["平成29年"].str.replace(",", ""))
df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",", ""))
df["人口増減"] = df["平成30年"] - df["平成29年"]
df = df.sort_values("人口増減", ascending=False)
df["人口増減"].plot.bar(figsize=(10, 6))
plt.show()

