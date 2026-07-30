import pandas as pd

R = pd.read_csv("tanks_data.csv")
print(R)

average = R["concentration_gL"].mean()
print(f"average :{average}")

F = R[(R["concentration_gL"] > 0.5) & (R["concentration_gL"] < 2.0)]
print(F)
