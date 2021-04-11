import numpy as np

class UnorderedArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def view(self):
        if self.last_position == -1:
            print('Array Emtpy')
        else:
            for i in range(self.last_position + 1):
                print(i, ': ', self.values[i])

    # O(1) - O(2)
    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print('Array Capacity Reached')
            return
        else:
            self.last_position += 1
            self.values[self.last_position] = value

    # O(n)
    def search(self, value):
        for i in range(self.last_position + 1):
            if value == self.values[i]:
                print(f'Value {value} founded at position: {i}')
                print("--------------")
                return i
        print(f'The value {value} isn\'t on array')
        print("--------------")
        return -1

    # O(n)
    def delete(self, value):
        position = self.search(value)
        if position == -1:
            return -1
        for i in range(position, self.last_position):
            self.values[i] = self.values[i + 1]
        self.last_position -= 1
        print(f'Value {value} removed ')
        print("--------------")

vector = UnorderedArray(5)

vector.view()

print("--------------")

vector.insert(1)
vector.insert(2)
vector.insert(3)
vector.insert(4)
vector.insert(5)

vector.view()

print("--------------")

vector.search(4)

vector.delete(5)

vector.view()
