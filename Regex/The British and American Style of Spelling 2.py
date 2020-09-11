# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

lines = []

N = int(input())
for i in range(N):
    x = input()
    lines.append(x)

T = int(input())
for i in range(T):
    x = input()
    y = x

    x = x.replace('our','or')
    pattern = re.compile('(?:\s|\A)'+'('+x+'|'+y+')'+'(?=\s|\Z)')
    
    count = 0
    for line in lines:
        count += len(re.findall(pattern, line))
    print(count)
