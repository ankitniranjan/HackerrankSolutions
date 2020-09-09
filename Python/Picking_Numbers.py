#!/bin/python3

import math
import os
import random
import re
import sys


def pickingNumbers(a):
    # Write your code here
    frequency = [0] * 100
    max_value = 0

    for number in a:
        frequency[number] += 1

    for i in range(1, 100):
        max_value = max(max_value, frequency[i] + frequency[i - 1])

    return(max_value)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
