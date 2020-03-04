import sys
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.suptitle("Battle: Army numbers of Nations A and B")

def battle(a, b, ak, bk):
    alist = [a]
    blist = [b]
    t = 0
    while a > 0 and b > 0:
        a -= b * bk
        b -= a * ak
        if a < 0 or b < 0:
            if a < 0:
                alist.append(0)
                blist.append(b)
            if b < 0:
                blist.append(0)
                alist.append(a)
        else:
            alist.append(a)
            blist.append(b)
        t += 1
    return alist, blist, t

def plot(alist, blist, t):
    tlist = list(range(t+1))

    plt.plot(tlist, alist)
    plt.plot(tlist, blist)
    plt.axis([0, max(tlist), 0, max([alist[0], blist[0]])])
    plt.show()


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    ak = int(sys.argv[3]) / 10000
    if len(sys.argv) == 4:
        bk = sys.argv[3]
    else:
        bk = sys.argv[4]
    bk = int(bk) / 10000

    alist, blist, t = battle(a, b, ak, bk)
    print(f'{alist}\n{blist}')
    plot(alist, blist, t)

main()