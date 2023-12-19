import random
import matplotlib.pyplot as plt


def draw():
    index= 0
    lottery = list(range(1,46))
    lucky_numb = []

    for i in range(6):
        index = random.randint(0, 44 - i)

        lucky_numb.append(lottery[index])

        lottery.append(lottery.pop(index))

    return lucky_numb


if __name__ == '__main__':

    print(draw())

    stats = []
    for x in range(46):
        stats.append(0)

    for i in range(1000000):
        for j in draw():
            stats[j] += 1
    print(stats)

    plt.bar(range(0, 46), stats)
    plt.xlabel("Numbers")
    plt.ylabel("Number of Draws")
    plt.title("Statistics")
    plt.show()





