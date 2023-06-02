# n = 7
# fact = 1
#
# for i in range(1, n + 1):
#     fact = fact * i
#
# print(fact)





class Node:

    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:   ### Связанный список.

    def __init__(self):
        self.head = Node()

    def add(self, value):
        if self.head.value is None:
            self.head.value = value
            return

        temp = Node()
        temp.value = value

        ###   1-й вариант.
        current_node = self.head
        print("current_node =", current_node.__dict__)

        while current_node.next is not None:
            current_node = current_node.next
        print("temp =", temp.__dict__)
        current_node.next = temp
        print("current_node.next =", current_node.next.__dict__)
        print("self.head =", self.head.__dict__)

        ###   2-й вариант.
        # temp.next = self.head
        # self.head = temp

ll = LinkedList()
ll.add(9)
ll.add(7)
ll.add(6)
ll.add(4)
ll.add(9)
ll.add(19)
a = 10


