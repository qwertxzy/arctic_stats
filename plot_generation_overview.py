import sys
import csv
import matplotlib.pyplot as plt

data = []
with open(sys.argv[1]) as csvfile:
  reader = csv.DictReader(csvfile, delimiter=',')
  for row in reader:
    data.append(row)

xpoints = [int(x['Generation']) for x in data]
ypoints_top = [float(x['Top']) for x in data]
ypoints_topfive = [float(x['Top5']) for x in data]
ypoints_avg = [float(x['Average']) for x in data]
ypoints_invalid = [float(x['Invalid']) for x in data]

fig, ax = plt.subplots()


ax.plot(xpoints, ypoints_top, label = "Best")
ax.plot(xpoints, ypoints_topfive, label = "Best 5 Avg")
ax.plot(xpoints, ypoints_avg, label = "Overall average")

ax.legend(loc="upper left")
ax.set_xlabel("Generation")
ax.set_ylabel("Fitness")

ax2 = ax.twinx()

ax2.plot(xpoints, ypoints_invalid, label="Invalid", color="red")

ax2.legend(loc="upper right")
ax2.set_xlabel("Generation")
ax2.set_ylabel("Invalid count")

plt.locator_params(axis="x", nbins=15)
plt.locator_params(axis="y", nbins=20)

plt.show()