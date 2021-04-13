import numpy as np

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = 0
        self.end = -1
        self.elements_lenght = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __empty(self):
        return self.elements_lenght == 0

    def __full(self):
        return self.elements_lenght == self.capacity

    def queue(self, value):
        if self.__full():
            print("Queue limit reached")
            return
        # this statement will be reached when end reached capacity of 
        # index and values was removed queues on another indexes
        # Example:
            # Consider following queue -  front [1, 3, 4, 5, 7] back
            # in this context start is index 0 and end is index 4
            # so dequeueing 2 items, start will be 2 and end still 4
            # now, let's add 5 value in queue
            # the end value could not be incremented because stack limit was reached
            # in this case we will reset end index, and point to queue start (and now is our end)
            # so now basically we have this:
            # [5, empty, 4, 5, 7] => end index is now 0, and start still 2
            # for this reason this queue called cirular, because what effectivelly changes is the start end end indexes
        if self.end == self.capacity -1:
            self.end = -1
        # add the value to end of queue
        self.end += 1
        self.values[self.end] = value
        # icrement queue elements
        self.elements_lenght += 1

    def dequeue(self):
        if self.__empty():
            print("Empty Queue")
            return
        
        # copy value to dequeue
        temp = self.values[self.start]
        # point start for the next value index
        self.start += 1
        # if start was on final of queue, we have to point to start index
        if self.start == self.capacity:
            self.start = 0
        # subtract array lenght
        self.elements_lenght -= 1
        # return removed value
        return temp

    def first(self):
        if self.__empty():
            return -1
        return self.values[self.start]

circular_queue = CircularQueue(5)

print(circular_queue.first())
print("--------------")

circular_queue.queue(1)
print(circular_queue.first())
print("--------------")

circular_queue.queue(3)
circular_queue.queue(4)
circular_queue.queue(5)
circular_queue.queue(7)
print(circular_queue.first())
print("--------------")

circular_queue.dequeue()
circular_queue.dequeue()
print(circular_queue.first())
print("--------------")

circular_queue.queue(5)
circular_queue.queue(7)
print(circular_queue.first())
print("--------------")

print(circular_queue.values)
print("--------------")

print(circular_queue.start, circular_queue.end)
print("--------------")