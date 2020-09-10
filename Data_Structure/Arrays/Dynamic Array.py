#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    lastAnswer_list = []
    seq = []
    
    for _ in range(n):
        seq.append([])

    for vals in queries:
        x,y=vals[1],vals[2] 
     
        if vals[0]==1:
            index=(x ^ lastAnswer) % n
            seq[index].append(y)
        else:
            index=(x ^ lastAnswer) % n
            size=y % len(seq[index])
            lastAnswer= seq[index][size]
            lastAnswer_list.append(lastAnswer)

    return lastAnswer_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
