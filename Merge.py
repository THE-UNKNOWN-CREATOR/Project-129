import pandas as pd
import csv

dataset1 = pd.read_csv("dwarf_stars.csv")
dataset1 = dataset1[dataset1["proper_name"].notna()]
dataset1 = dataset1[dataset1["distance"].notna()]
dataset1 = dataset1[dataset1["mass"].notna()]
dataset1 = dataset1[dataset1["radius"].notna()]

radius = dataset1["radius"].to_list()
for index, i in enumerate(radius):
    i = float(float(i)*0.102763)
    radius[index] = i
print(radius)

masses = dataset1["mass"].to_list()
for index, i in enumerate(masses):
    i = float( float(i) *0.000954588)
    masses[index] = i
print(masses)

dataset1["radius"] = radius
dataset1["mass"] = masses

dataset1.to_csv("dwarf_stars.csv", index=False)

star_data = []
dwarf_data = []

with open("star_data.csv") as star:
    data = csv.reader(star)
    for row in data:
        star_data.append(row)
with open("dwarf_stars.csv") as dwarf:
    data = csv.reader(dwarf)
    for row in data:
        dwarf_data.append(row)

data1 = star_data[1:]
data2 = dwarf_data[1:]

header = star_data[0]

final_data = []
ind = 0

for i in data1:
    final_data.append(i)
    ind += 1

for i in data2:
    i[0] = int(i[0]) + ind
    final_data.append(i)

with open("merged.csv", "w", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(final_data)