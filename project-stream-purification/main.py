import pandas as pd

R = pd.read_csv("stream_data.csv")
print(R)

R["pure_flow_kgh"] = R["flow_rate_kgh"] * (R["purity_percent"] / 100)

missing_rows = R[R.isna().any(axis=1)]
print(missing_rows)

sort = R.sort_values(by="pure_flow_kgh", ascending=False)
print(sort)

Filtering = R[(R["status"] == "active") & (R["pure_flow_kgh"] > 150)]
print(Filtering)
