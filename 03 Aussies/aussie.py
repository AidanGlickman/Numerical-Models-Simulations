import csv
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.suptitle("Population vs Time")

with open('aussiepopulation.csv', mode='r') as infile:
    reader = csv.reader(infile)
    popdict = {int(rows[0]):float(rows[1]) for rows in reader}
years = popdict.keys()
pops = popdict.values()

x = np.array(list(years))
y = np.array(list(pops))
np.polyfit(np.log(x), y, 1)

# plt.plot(years, pops)
# plt.axis([min(years), max(years), min(pops), max(pops)])
# plt.show()