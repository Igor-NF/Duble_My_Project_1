class Node:

    def __init__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return f"[{self.value}]->{self.next}"

class LinkedList:

    def __init__(self):
        self.head = Node()


    def __str__(self):
        return str(self.head)


    def add(self, val):
        if self.head.value is None:
            self.head.value = val
            return
        temp = Node()
        temp.value = val
        # temp.next = self.head
        self.head = temp


ll = LinkedList()
ll.add(4)
ll.add(5)
ll.add(6)
a = 1
