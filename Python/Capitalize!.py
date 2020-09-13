#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # return s.title() 
    # This will capatalize first characters of the word 
    # It has one problem
    # if s = 123ws it will change to s = 123Ws

    # This problem can be solved by using capitalize() method.

    return ' '.join([i.capitalize() for i in s.split(' ')])
    # [] =>list of words
    # ' '.join([]) =>string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
