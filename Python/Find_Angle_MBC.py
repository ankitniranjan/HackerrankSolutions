import math
import cmath
# Enter your code here. Read input from STDIN. Print output to STDOUT
AB = int(input())
BC = int(input())

#in figure BC == BM (property)
#thus deg(MBC) == deg(BCA)
#thus angle btw BCA is (below) 
print(str(int(round(math.degrees(cmath.phase(complex(BC,AB))))))+'°')
