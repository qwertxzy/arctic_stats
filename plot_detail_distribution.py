import sys
import csv
import matplotlib.pyplot as plt

data = []
with open(sys.argv[1]) as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    data.append(row)

xvalues = []
yvalues = []

generation_ctr = 0
for generation in data:
  xvalues.extend([generation_ctr] * len(generation))
  yvalues.extend([float(i) for i in generation])
  generation_ctr += 1


plt.hist2d(xvalues, yvalues, bins=(int(150 / 2), 40), cmap=plt.cm.jet)
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.colorbar()
plt.show()
