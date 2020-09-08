import cmath
# Enter your code here. Read input from STDIN. Print output to STDOUT
num = complex(input())
x = int(num.real)
y = int(num.imag)

print(abs(complex(x,y)))
print(cmath.phase(complex(x,y)))
