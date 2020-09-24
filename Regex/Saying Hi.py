# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'^[Hh][Ii]\s[^Dd].*$'

n = int(input())
for _ in range(n):
    result = re.search(pattern, input())
    if result:
        print(result.group())
