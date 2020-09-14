#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swap = 0
    n = len(a)
	
    for i in range(n):   
        for j in range(n - 1): 
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]:
                swap += 1
                a[j], a[j + 1] = a[j + 1], a[j]
				
    print('Array is sorted in {} swaps.'.format(swap))
    print('First Element:',a[0])
    print('Last Element:',a[n-1])
        

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
