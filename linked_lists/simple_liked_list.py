import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def show_node(self):
        print(self.value)

class LinkedList:
    def __init__(self):
        self.first = None

    def start_insert(self, value):
        new = Node(value)
        new.next = self.first
        self.first = new
        
    def show(self):
        if self.first == None:
            print('Empty List')
            return None
        current = self.first
        while current != None:
            current.show_node()
            current = current.next

    def search(self, value):
        if self.first == None:
            print('Empty List')
            return None
        
        current = self.first
        while current.value != value:
            if current.next is None:
                print("Value not found")
                return None
            else:
                current = current.next

        return current

    def start_delete(self):
        if self.first == None:
            print('Empty List')
            return None
        temp = self.first
        self.first = self.first.next
        return temp

    def position_delete(self, value):
        # the search begin from list firt item
        current = self.first
        # previous value has to be saved because him points to next from the item deleted
        previous = self.first

        # while current value is different then seached, this block will be executed
        while current.value != value:
            # if has no value after, the value could not be found
            if current.next == None:
                return None
            else:
                # otherwise previous is now current
                previous = current
                # and current is next value
                current = current.next
        # when the value was found is the first on the list
        if current == self.first:
            # now the first value is the next of first
            self.first = self.first.next
        else:
            # otherwise the previous pointer to next value of found
            previous.next = current.next

        #returning value found
        return current

linked_list = LinkedList()

linked_list.start_insert(1)

linked_list.start_insert(2)

linked_list.start_insert(3)
linked_list.start_insert(4)
linked_list.start_insert(5)
linked_list.start_insert(6)

linked_list.show()

'''
linked_list.start_delete()
linked_list.start_delete()
linked_list.start_delete()
linked_list.start_delete()
linked_list.start_delete()
linked_list.start_delete()

linked_list.show()
'''

print(linked_list.search(5).value)

print(linked_list.position_delete(4).value)

linked_list.show()