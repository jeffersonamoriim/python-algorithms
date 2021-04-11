import numpy as np

class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = np.chararray(self.__capacity, unicode=True)

    def __stack_overflow(self):
        if self.__top == self.__capacity - 1:
            return True
        return False

    def empty_stack(self):
        if self.__top == -1:
            return True
        return False
    
    def stack_up(self, value):
        if self.__stack_overflow():
            print('Stack Overflow')
        else:
            self.__top += 1
            self.__values[self.__top] = value
    
    def unstack(self):
        if self.empty_stack():
            print('Empty Stack')
        else:
            value = self.__values[self.__top]
            self.__top -= 1
            return value

    def view_top(self):
        if self.__top != -1:
            return self.__values[self.__top]
        else:
            return -1

expression = str(input('type the expression: '))
stack = Stack(len(expression))

# the openers and closers are on priority level
openers = ['{', '[', '(']
closers = ['}', ']', ')']

# this function only store openers
for i in range(len(expression)):
    # store value on expression index
    ch = expression[i]
    # if char is on openers stack up
    if ch in openers:
        stack.stack_up(ch)
    # otherwise, if char is on closers
    elif ch in closers:
        # validade if stack are not empty because closes need openers
        if not stack.empty_stack():
            # store the last opener on stack
            chx = str(stack.unstack())
            # validate if the opener is diferent of the closer to provide some error
            if (ch == closers[0] and chx != openers[0]) or (ch == closers[1] and chx != openers[1]) or (ch == closers[2] and chx != openers[2]):
                print("Error: ", ch, ' at position', i)
                break
        else:
            print("Error: ", ch, ' at position', i)
            
if not stack.empty_stack():
    print('error')