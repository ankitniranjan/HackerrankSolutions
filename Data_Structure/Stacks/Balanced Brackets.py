#!/bin/python3

import os
import sys

# Complete the isBalanced function below.

# Without Using Stack
def isBalanced(s):
    restart=True
    while restart:
        if '{}' in s:
            s=s.replace('{}','')
        elif '()' in s:
            s=s.replace('()','')
        elif '[]' in s:
            s=s.replace('[]','')
        else:
            restart=False
    return 'YES' if len(s)==0 else 'NO'


# Using Stack
def isBalanced(s):
    # Complete this function
    bracket_map = {'{': '}', '(': ')', '[': ']'}
    stack = []
    for b in s:
        if b in bracket_map.keys():  # openning
            stack.append(bracket_map[b])
        elif b in bracket_map.values():  # closing
            if not stack or stack.pop() != b:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
