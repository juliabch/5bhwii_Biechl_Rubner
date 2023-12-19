import random
import matplotlib.pyplot as plt

throws = []
tries = 100000


def throw_dice():
    index = 0
    single = list(random.sample(range(1, 7), 1))

    for i in range(1):
        throws.append(single[index])

    return throws


if __name__ == '__main__':

    print(throws)

    stats = {}
    # for x in range(0, 6):
    #   stats.append(0)

    for i in range(tries):
        for j in throw_dice():
            if j in stats:
                stats[j] += 1
            else:
                stats[j] = 1
    print(stats)

    plt.bar(stats.keys(), stats.values())
    plt.xlabel("Number")
    plt.ylabel("Number of tries")
    plt.title("Stats")
    plt.show()
