# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
original = set(map(int, input().split()))

loop = int(input())

for i in range(loop):
    operation, length = input().split()

    if operation == 'intersection_update':
        values = set(map(int, input().split()))
        original.intersection_update(values) 
    elif operation == 'update':
        values = set(map(int, input().split()))
        original.update(values) 
    elif operation == 'symmetric_difference_update':
        values = set(map(int, input().split()))
        original.symmetric_difference_update(values) 
    elif operation == 'difference_update':
        values = set(map(int, input().split()))
        original.difference_update(values) 

print(sum(original))
