# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
regex = r'(hackerrank)'
pattern = re.compile(regex, re.IGNORECASE)

def validate(line):
    return re.search(pattern, line)
	
n = int(input())
count = 0

for _ in range(n):
    line = input()
    if validate(line):
        count += 1
print(count)
