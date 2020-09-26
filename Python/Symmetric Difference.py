# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
Ms = set(map(int, input().split()))

N = int(input())
Ns = set(map(int, input().split()))

result = sorted((Ms.union(Ns)) - (Ms.intersection(Ns)))
print(*result, sep='\n')
