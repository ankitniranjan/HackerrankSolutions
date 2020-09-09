#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    for i in s:
        if i == 'a':
            count += 1
    no_of_repeatetion = n//len(s)
    
    ans = count*no_of_repeatetion

    remainder = n%len(s)
    for i in range(remainder):
        if s[i] == 'a':
            ans += 1
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
