# Enter your code here. Read input from STDIN. Print output to STDOUT
n,  m = input().split()

n_array  = [int(x) for x in input().split()]
A = set([int(x) for x in input().split()])
B = set([int(x) for x in input().split()])

A = A.difference(B)  #Making Both sets disjoint
B = B.difference(A)

happiness = 0
for i in n_array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)
