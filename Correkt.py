class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}]->{self.next}"

class LinkedList:
    def __init__(self):
        self.head = Node

    def __str__(self):
        return str(self.head)


if __name__ == "__main__":
    linked_list = LinkedList()
    temp = Node(1)
    linked_list.head = temp
    for i in (3, 5, 7, 9):
        temp.next = Node(i)
        temp = temp.next

print(linked_list)



# n = Node(5)
# n1 = Node(1)
# n2 = Node(7)
# n.next = n1
# n1.next = n2
# print(n)
a = 1
