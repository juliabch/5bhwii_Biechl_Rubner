class Node:
    def __init__(self, age):
        self.age = age
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, age):
        new_node = Node(age)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.age)
            cur_node = cur_node.next

    def get_length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    # implement the iterator protocol
    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node.age
            cur_node = cur_node.next

    def calc_middle(self):
        cur_node = self.head
        lastsum = 0
        while cur_node:
            lastsum += cur_node.age
            cur_node = cur_node.next
        calc_middle = lastsum / self.get_length()
        print("sum")
        print(lastsum)
        print("length")
        print(self.get_length())
        return calc_middle
