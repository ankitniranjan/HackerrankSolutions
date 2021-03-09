
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#
alphabets = ['1','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
array = []
def getTime(s):
    # Write your code here
    s = s.lower()
    if s[0] != 'a':
        s = 'a' + s
    sum = 0
    for char in s:
        array.append(alphabets.index(char))
   
    for i in range(len(array)-1):
        x = abs(array[i+1] - array[i])
        y = 26 - x
        
        if x > y:
            sum += y
        else:
            sum += x
    return(sum)
         
if __name__ == '__main__':
