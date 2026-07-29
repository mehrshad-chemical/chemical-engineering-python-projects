import json
import csv

data_lab ={
    "experiment": "Concentration Decay",
    "initial_concentration": 1.0,
    "measurements": [
        {"time": 0, "c": 1.0},
        {"time": 10, "c": 0.8},
        {"time": 20, "c": 0.65},
        {"time": 30, "c": 0.5}
    ]
}

input_file = "lab_data.json"
output_file = "composite_report.csv"

with open(input_file,mode="w") as f:
    json.dump(data_lab,f)

with open("lab_data.json", mode="r") as f:
    file = json.load(f)

measurements = file["measurements"]


results = []


for i in range(len(measurements) -1):
    t1 = measurements[i]["time"]
    t2 = measurements[i+1]["time"]
    c1 = measurements[i]["c"]
    c2 = measurements[i+1]["c"]
    rate = -(c2 - c1) / (t2 - t1)

    results.append({"Interval": f"{t1}-{t2}","Rate":rate})

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Interval", "Rate"])
    writer.writeheader()
    writer.writerows(results)


print(f"Results saved to {output_file}")
