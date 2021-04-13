import numpy as np


class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = -1
        self.end = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __full(self):
        return (self.start == 0 and self.end == self.capacity - 1) or (self.start == self.end + 1)

    def __empty(self):
        return self.start == -1

    def start_insert(self, value):
        if self.__full():
            print("Deque limit reached")
            return

        # if empty
        if self.start == -1:
            self.start = 0
            self.end = 0
        # if start was on first position, adds start to end of array
        # on this case the array will be like => END [n1, n2, n3, ... ] START
        # so start values was inserted from the right to the left on the left side
        # Example:
            # consider the following empty array => [ empty, empty, emtpy, empty ]
            # next, lets start insert the value 3, the array will be => [ empty, empty, emtpy, 3]
            # in this case, start pointer now is on index 3 and end pointer the same
            # now lets insert the value 2, the array will be => [ empty, emtpy, 2, 3]
            # in this case, start pointer now is on index 2, and end index on index 3
            # so if you want to start remove you will remove value 2, if end remove value 3
        elif self.start == 0:
            self.start = self.capacity - 1
        else:
            self.start -= 1

        self.values[self.start] = value

    def end_insert(self, value):
        if self.__full():
            print("Deque limit reached")
            return

        # if empty update end and start position to same value
        if self.start == -1:
            self.start = 0
            self.end = 0
        # if end was on last position, adds end to start of array
        # on this case the array will be like => END [n1, n2, n3, ... ] START
        # so end values was inserted from the left to the right on the right side
        # Example:
            # consider the following empty array => [ empty, empty, emtpy, empty ]
            # next, lets end insert the value 3, the array will be => [ 3, empty, emtpy, empty]
            # in this case, end pointer now is on index 0 and end pointer the same
            # now lets insert the value 2, the array will be => [ 3, 2, empty, empty]
            # in this case, end pointer now is on index 1, and start index on index 0
            # so if you want to end remove you will remove value 2, if end start value 3
        elif self.end == self.capacity - 1:
            self.end = 0
        # if end was on last position, adds start to beginning of array
        # on this case the array will be like => END [n1, n2, n3, ... ] START
        # so end values was inserted from the right to left
        else:
            self.end += 1

        self.values[self.end] = value

    def start_delete(self):
        if self.__empty():
            print("Deque Empty")
            return

        # if has only one element
        if self.start == self.end:
            self.start = -1
            self.end = -1
        else:
            # back to start
            if self.start == self.capacity - 1:
                self.start = 0
            else:
                # increment start to remove current start
                self.start += 1

    def end_delete(self):
        if self.__empty():
            print("Deque Empty")
            return

        # if has only one element
        if self.start == self.end:
            self.start = -1
            self.end = -1
        elif self.start == 0:
            self.start = self.capacity - 1
        else:
            self.end -= 1

    def get_start(self):
        if self.__empty():
            print("Deque Empty")
            return

        return self.values[self.start]

    def get_end(self):
        if self.__empty():
            print("Deque Empty")
            return

        return self.values[self.end]


deque = Deque(5)

# 5 0 0 0 0
deque.end_insert(5)
print("End Insert of value 5")
print('[{}:{}]'.format(deque.get_start(), deque.get_end()))
print(f'END  - {deque.values} - START')
print('(start_index: {} - end_index: {})'.format(deque.start, deque.end))
print("--------------")

# 5 10 0 0 0
deque.end_insert(10)

print("End Insert of value 10")
print('[{}:{}]'.format(deque.get_start(), deque.get_end()))
print(f'END  - {deque.values} - START')
print('(start_index: {} - end_index: {})'.format(deque.start, deque.end))
print("--------------")

# 5 10 0 0 3
deque.start_insert(3)

print("Start insert of value 3")
print('[{}:{}]'.format(deque.get_start(), deque.get_end()))
print(f'END  - {deque.values} - START')
print('(start_index: {} - end_index: {})'.format(deque.start, deque.end))
print("--------------")

# 5 10 0 2 3
deque.start_insert(2)
print("Start insert of value 2")
print('[{}:{}]'.format(deque.get_start(), deque.get_end()))
print(f'END  - {deque.values} - START')
print('(start_index: {} - end_index: {})'.format(deque.start, deque.end))
print("--------------")

# 5 10 11 2 3
deque.end_insert(11)
print("End Insert of value 11")
print('[{}:{}]'.format(deque.get_start(), deque.get_end()))
print(f'END  - {deque.values} - START')
print('(start_index: {} - end_index: {})'.format(deque.start, deque.end))
print("--------------")

deque.start_delete()
deque.end_delete()
print("One end and start delete")
print('[{}:{}]'.format(deque.get_start(), deque.get_end()))
print(f'END  - {deque.values} - START')
print('(start_index: {} - end_index: {})'.format(deque.start, deque.end))
print("--------------")

deque.start_delete()
print("One start delete")
print('[{}:{}]'.format(deque.get_start(), deque.get_end()))
print(f'END  - {deque.values} - START')
print('(start_index: {} - end_index: {})'.format(deque.start, deque.end))
print("--------------")
