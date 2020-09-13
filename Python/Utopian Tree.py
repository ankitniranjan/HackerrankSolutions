#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    if n==0:
        return(1)
    else:
        height = 1
        flag = True
        for i in range(n):
            if flag == True:
                height = 2*height
                flag = False
            else: 
                height += 1
                flag = True
        return(height)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
