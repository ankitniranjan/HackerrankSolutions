def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        l=len('{0:b}'.format(number))   #n=2 binary=01 len=2 
        l=int(l)
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i,width=l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
