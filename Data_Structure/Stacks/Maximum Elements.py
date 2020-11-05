# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    stack = []
    n = int(input())
    for i in range(n):
        items = list(map(int, input().split()))
        if items[0] == 1:
            stack.append(items[1])
        elif items[0] == 2:
            stack.pop()
        else:
            print(max(stack))
