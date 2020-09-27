# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    try:
        a, b = map(int, input().split())
        res = a//b
        print(res)
    except Exception as e:
        print('Error Code:',e)
------------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    try:
        a, b = map(int, input().split())
        res = a//b
        print(res)
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)
