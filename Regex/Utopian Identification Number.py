# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'

n = int(input())
for _ in range(n):
    result = re.search(pattern, input())
    if result:
        print('VALID')
    else:
        print('INVALID')
