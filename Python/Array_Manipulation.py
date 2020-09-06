#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    maximum_int_value = 0
    current_int_value  = 0
    arr = [0]*n
    for query in queries:
        arr[query[0] - 1] += query[2]
        if query[1] != len(arr):
            arr[query[1]] -= query[2]
    for i in range(len(arr)):
        current_int_value  += arr[i]
        if maximum_int_value < current_int_value :
            maximum_int_value = current_int_value 

    return maximum_int_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
