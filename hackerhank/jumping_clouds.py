#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    index = 0

    has_next = lambda position: len(c) > position

    for i in range(len(c)):
        has_next_value = has_next(index + 1)
        if index > i:
            pass
        elif has_next_value:
            if c[index] == 0 and c[index -1] == 1:
                jumps += 1
                index += 1
            elif c[index] == 0 and c[index + 1] == 0:
                jumps += 1
                index += 2
            elif c[index] == 0:
                jumps += 1
                index += 1
            else:
                index +=1
        elif c[index] == 0:
            jumps += 1
            index += 1

    print(len(c) % 2)
            
    return jumps
        

n = int(input())

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c)

print(result)
