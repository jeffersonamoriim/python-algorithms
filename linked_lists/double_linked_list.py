import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def show_node(self):
        print(self.value)

class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def __empty(self):
        return self.first == None
    
    def start_insert(self, value):
        new = Node(value)
        # if list is empty last = first
        if self.__empty():
            self.last = new
        # new.next is the current first because we moving him up
        new.next = self.first
        # first now is the value received
        self.first = new

    def end_insert(self, value):
        new = Node(value)
        if self.__empty():
            self.first = new
        else:
            # the last item is now the item created, so actual last has to poit to him
            self.last.next = new
        self.last = new

    def start_delete(self):
        if self.__empty():
            print("Empty List")

        temp = self.first
        # if has only one value on the list
        if self.first.next == None:
            self.last = None
        self.first = self.first.next
        return temp
        
        

    def show(self):
        if self.__empty():
            print('Empty List')
            return
        current = self.first
        while current != None:
            current.show_node()
            current = current.next

double_linked_list = DoubleLinkedList()

double_linked_list.start_insert(1)

double_linked_list.start_insert(2)

double_linked_list.end_insert(9)

double_linked_list.end_insert(11)

double_linked_list.start_insert(7)

double_linked_list.start_delete()

double_linked_list.start_delete()

double_linked_list.show()