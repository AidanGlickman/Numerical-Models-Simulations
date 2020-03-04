import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.suptitle("Population vs Time")

pop = 100000
k = 0.01

x = []
y = []

for t in range(0, 50, 1):
    popPrime = pop*k
    x.append(t)
    y.append(pop)
    print("Population: %.2f Population': %.2f Time: %.2f" % (pop, popPrime, t))
    pop += popPrime * t/10

plt.plot(x, y)
plt.axis([0, max(x), 0, max(y)])
plt.show()