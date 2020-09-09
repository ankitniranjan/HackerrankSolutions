#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    for pos, val in enumerate(q):
        if val - (pos+1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0,val-3), pos):
            if q[j] > val:
                moves+=1
    print(moves)
    return
    
#     OR

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = 0
    for i in range(len(q)):
        if q[i] - (i + 1) >= 3:
            print("Too chaotic")
            return
    ongoing = True
    last_index = 0
    while ongoing:
        for i in range(last_index, len(q)-1):
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                if i > 0:
                    last_index = i-1
                n += 1
                break
        else:
            ongoing = False
    print(n)
    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
