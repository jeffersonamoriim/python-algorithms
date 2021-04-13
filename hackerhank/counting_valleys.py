#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    level = 0
    vars = {
        'U': 1,
        'D': -1
    }
    
    down_sea = 0
    valleys = 0
    
    for i in range(steps):
        level += vars[path[i]]
        if level == -1:
            down_sea += 1
        if down_sea >= 1 and level == 0:
            valleys += 1
            down_sea = 0
            
    return valleys
    
steps = int(input().strip())

path = input()

result = countingValleys(steps, path)

print(result)
