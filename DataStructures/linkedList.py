""" Linked List --> Linear data structure , unlike Array elements can be stored at any 
    memory address which need not to be contigous. Singly linked list --> consists of Nodes which contains
    two properties which is data and next pointer"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        print("The elements of the linked list are:")
        while temp:
            print(temp.data, end="\n", )
            temp = temp.next

    def push_first(self, newData):

        temp = Node(newData)
        temp.next = self.head
        self.head = temp

    def push_middle(self, prev, newData):

        if prev is None:
            print("Previous Node should be present!")
            return
        temp = Node(newData)
        temp.next = prev.next
        prev.next = temp


if __name__ == '__main__':

    list = linkedList()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    list.head.next = second
    second.next = third

    list.printList()
    list.push_first(4)
    list.printList()
    list.push_middle(third, 5)
    list.printList()
