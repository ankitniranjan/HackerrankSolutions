if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    top = max(arr)
    l  = [i for i in arr if i != top]
    print(max(l))
