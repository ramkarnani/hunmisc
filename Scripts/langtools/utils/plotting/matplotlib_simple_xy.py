import sys

import matplotlib.pyplot as plt

def read_data(istream):
    r = [[],[],[],[],[]]
    for l in istream:
        le = l.strip().split()
        [r[i].append(le[i]) for i in xrange(len(le))]
    return r

def main():
    d = read_data(open(sys.argv[1]))
    ax = plt.subplot(111)
    ax.plot(d[0], d[1], label="$M$")
    ax.plot(d[0], d[2], label="$l KL$")
    ax.plot(d[0], d[3], label="$l (H_q+KL)$")
    ax.plot(d[0], d[4], label="$M + l (H_q+KL)$")
    plt.xlabel("Bits")
    ax.legend(loc=7)
    plt.show()
    #plt.savefig("fig.png")

if __name__ == "__main__":
    main()
