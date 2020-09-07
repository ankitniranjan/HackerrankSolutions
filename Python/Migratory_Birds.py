#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
# Using List
def migratoryBirds(arr):
    l= [0]*6
    for i in arr:
        l[i] += 1
    k = max(l) #returns first max value

    #here we're ignoring type-0 and index-0
    return(l.index(k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
