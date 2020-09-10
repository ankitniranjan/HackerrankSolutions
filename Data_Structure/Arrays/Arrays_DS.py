#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    l = int(len(a)/2)
    n = len(a)
    for i in range(0,l):
        a[i], a[n-1-i] = a[n-1-i] ,a[i]
    return (a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
