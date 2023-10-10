import random
import matplotlib.pyplot as plt


def draw():
    index = 0
    lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
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





