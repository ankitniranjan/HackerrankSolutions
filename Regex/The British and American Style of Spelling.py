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
    x = x[:len(x)-2]

    count = 0
    result = re.compile(x+'(se|ze)')    # x(se|ze)

    for line in lines:
        count += len(re.findall(result, line))
    print(count)
