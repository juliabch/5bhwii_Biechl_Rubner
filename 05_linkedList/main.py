import random
from linledList import LinkedList

if __name__ == '__main__':

    a = LinkedList()
    for _ in range(10):
        a.append(random.randint(1, 100))
    print("print list")
    a.print_list()
    # print length
    print("print length")
    print(a.get_length())
    # use the iterator
    print("use iterator")
    for node in a:
        print(node)
    # calc the average
    print("calced Average")
    print(a.calc_middle())