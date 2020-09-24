# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern1 = r'^(hackerrank).+'
pattern2 = r'.+(hackerrank)$'
pattern3 = r'^(hackerrank)$'

n = int(input())

for _ in range(n):
    line = input()
    if re.search(pattern1, line):
        print('1')
    elif re.search(pattern2, line):
        print('2')
    elif re.search(pattern3, line):
        print('0')
    else:
        print('-1')
