# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):
    len_A = int(input())
    A = set(map(int, input().split())) 

    len_B = int(input())
    B = set(map(int, input().split())) 

    if A.issubset(B):
        print('True')
    else:
        print('False')
