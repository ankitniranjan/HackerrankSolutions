>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]

---------------------------------------------------------------

from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT

X = input()
S = Counter(map(int,input().split()))

N = int(input())
earnings = 0
for customer in range(N):
    size, x_i = map(int,input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i
            
print(earnings) 
