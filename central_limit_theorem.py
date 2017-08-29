from collections import Counter
import numpy as np
from matplotlib import pyplot as plt
import bisect

def sampleN(n, items, probs):
    values = [0]*n
    for i in range(n):
        values[i] = sample(items, probs)
    return values


def sample(items, probs):
    csum = np.cumsum(probs)
    r = np.random.rand()
    idx = find_idx(csum, r)
    if idx >= 0:
        return items[idx]
    else:
        return items[0]

def find_idx(csum, r):
    return bisect.bisect(csum, r)

def run_sim_central_limit(items, probs, values,steps):
    c = Counter()
    c.update([np.mean(sampleN(values,items, probs)) for i in range(steps)])
    return c

def plot(x,y):
    order = np.argsort(x)
    xsorted = x[order]
    ysorted = y[order]
    plt.plot(xsorted, ysorted, color='b')
    plt.xlabel('Mean of the Sample')
    plt.ylabel('Frequency of the Means')
    plt.title('Central Limit Theorem Demo')
    plt.scatter(x, y, color='r')
    plt.show()

def main():
    probs = np.asarray([1.0/6] * 6)
    items = np.arange(1,7)
    print("Running Simulation...")
    c = run_sim_central_limit(items, probs, 3, 1000000)
    print("Generating the plot")
    plot(np.asarray(c.keys()), np.asarray(c.values()))


if __name__ == "__main__":
    main()

