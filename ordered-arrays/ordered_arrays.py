import numpy as np

class OrderedArray:
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
    # O(n)
    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print('Array Capacity Reached')
            return
        
        # variable of value position on array
        position = 0

        # loop to search de value position
        for i in range(self.last_position + 1):
            position = i
            # if value on array is greater then value provided, means the position of value is i, so just break
            # Example:
                # array = [2, 5, 8, 9] -> value = 3
                # so 3 is greater than 2, and i is 1, so the positions to store the value 3 is 1
            if self.values[i] > value:
                break
            # if the value is greater than last position, means that him is greater than our last value
            # so the position for him is the last
            if i == self.last_position:
                position = i + 1
                

        # now we need to sweet array back to front to move other values on array, so x is the last postition
        x = self.last_position
        # we have a position to save the value provided, so now lets move another value
        # while x is greater or equal than position to our value we just move the currents values up
        while x >= position:
            # Example:
            # array = [2, 5, 8, 9] -> value = 3
            # value 3 has to saved on position 1, so 5, 8 and 9 has to move up
            # initialy x is 3, so 3 + 1 = 4, position 4 now has the value 9
            # next x is 2, so 2 + 1 = 3, position 3 now has the value 8
            # next x is 1, so 1 + 1 = 2, position 2 now has the value 5
            self.values[x + 1] = self.values[x]
            x -=1

        # the value position is empty now, so just save him on it
        self.values[position] = value

        # don't forget to increment our last position value
        self.last_position += 1
    
    # O(n)
    def search(self, value):
        for i in range(self.last_position + 1):
            # if some value on array is greater than value provided means that him isn't on array
            if self.values[i] > value:
                print(f'The value {value} isn\'t on array')
                print("--------------")
                return -1
            if self.values[i] == value:
                print(f'Value {value} founded at position: {i}')
                print("--------------")
                return i
            # if was passed on all array means that value provided isn't on array
            if i == self.last_position:
                print(f'The value {value} isn\'t on array')
                print("--------------")
                return -1

    # (log(n))
    def binary_search(self, value):
        lower_limit = 0
        upper_limit = self.last_position

        while True:
            # this step center the position, so (lower_limit + upper_limit) / 2 = middle of array context
            current_position = int((lower_limit + upper_limit) / 2)
            if self.values[current_position] == value:
                print(f'Value {value} founded at position: {current_position}')
                print("--------------")
                return current_position
            elif lower_limit > upper_limit:
                # if lower limit is greater than upper means that you search on entirely array, not found
                print(f'The value {value} isn\'t on array')
                print("--------------")
                return -1
            else:
                # if value on the current position is lower than value provided means the lower_limit
                # is now the value + 1
                # Example:
                    # consider 53 as value provided and, 50 as value of current position
                    # 50 is lower than 53, so our value is above 50
                    # it means that our value is after the current index
                if self.values[current_position] < value:
                    lower_limit = current_position + 1
                # otherwise, if the value on current position is greater than value provided, means the upper_limit
                # is now the value - 1
                # Example:
                    # consider 50 as value provided and, 53 as value of current position
                    # 53 is greater than 50, so our value is bellow 53
                    # it means that our value is before the current index
                else:
                    upper_limit = current_position - 1

    # O(n)
    def delete(self, value):
        position = self.search(value)
        if position == -1:
            return -1
        for i in range(position, self.last_position):
            # reajusting values to new positions
            # moving the remaining values one index bellow
            self.values[i] = self.values[i + 1]
        self.last_position -= 1
        print(f'Value {value} removed ')
        print("--------------")


vector = OrderedArray(10)

vector.view()

print("--------------")

vector.insert(5)

vector.view()

print("--------------")

vector.insert(2)

vector.view()

print("--------------")

vector.insert(7)

vector.view()

print("--------------")

vector.search(9)

vector.delete(2)


vector.view()

print("--------------")

