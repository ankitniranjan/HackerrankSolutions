# Enter your code here. Read input from STDIN. Print output to STDOUT
from re import findall

n = int(input())
para = []
for i in range(n):
    para.append(input())

para = ' '.join(para)
q = int(input())
for i in range(q):
    subword = input()
    print(len(findall('\w+(' + subword + ')\w+', para)))
