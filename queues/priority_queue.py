import numpy as np


class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements_lenght = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __empty(self):
            return self.elements_lenght == 0

    def __full(self):
        return self.elements_lenght == self.capacity

    def queue(self, value):
        if self.__full():
            print("Queue Limit Reached")
            return
        # if queue has no elements
        if self.elements_lenght == 0:
            # add the value to fist index
            self.values[self.elements_lenght] = value
            # increment index
            self.elements_lenght += 1
        # otherwise
        else:
            # x is the current last position
            x = self.elements_lenght - 1
            # while last position is greater or equal than 0
            while x >= 0:
                # if value received is greater then value in position x, the priority of him is lower of the current value on x index
                # Example:
                    # Consider the following queue => [30, empty, emtpy, emtpy, empty], and the value provided 50
                    # 30 is lower than 50, so him has priority
                    # to do this we move 30 to next position
                    # the queue will be like => [empty, 30, empty, empty, empty]
                    # this basically reorder the elemtents
                if value > self.values[x]:
                    self.values[x + 1] = self.values[x]
                # othewise break
                else:
                    break
                # aways decrement x
                x -= 1
            # continuing the example now the index x is equal then previously used by 30, so 50 has to be on this index
                # in this line queue will be like => [50, 30, empty, empty, empty]
            self.values[x + 1] = value
                # elements is two 
            self.elements_lenght += 1

    def dequeue(self):
        if self.__empty():
            print('Empty Queue')
        
        # simple remove first item 
        temp = self.values[self.elements_lenght - 1]
        self.elements_lenght -= 1
        return temp

    def first(self):
        if self.__empty():
            return -1
        return self.values[self.elements_lenght - 1]

priority_queue = PriorityQueue(5)

print(priority_queue.first())
print("--------------")

# BACK 30 FRONT
priority_queue.queue(30)
print(priority_queue.first())
print("--------------")

# BACK 50 30 FRONT
priority_queue.queue(50)
print(priority_queue.first())
print("--------------")

# BACK 50 30 10 FRONT
priority_queue.queue(10)
print(priority_queue.first())
print("--------------")

# BACK 50 40 30 10 FRONT
priority_queue.queue(40)
print(priority_queue.first())
print("--------------")

# BACK 50 40 30 20 10 FRONT
priority_queue.queue(20)
print(priority_queue.first())
print("--------------")

print(priority_queue.values)
print("--------------")

priority_queue.dequeue()
print(priority_queue.first())
print("--------------")

priority_queue.dequeue()
print(priority_queue.first())
print("--------------")

priority_queue.dequeue()
print(priority_queue.first())
print("--------------")

priority_queue.queue(5)
print(priority_queue.first())
print("--------------")

print(priority_queue.values)
print("--------------")

