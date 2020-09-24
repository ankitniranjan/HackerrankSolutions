# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

n = int(input())
for _ in range(n):
    result = re.search(pattern, input())
    if result:
        print('YES')
    else:
        print('NO')
