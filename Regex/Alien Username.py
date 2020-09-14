# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
regex_exp = r"^[_.]\d+[a-zA-Z]*(_)?$"
regex_exp = re.compile(regex_exp)

n = int(input())

for i in range(n):
    s = input()
    if re.match(regex_exp, s):
        print('VALID')
    else:
        print('INVALID')
