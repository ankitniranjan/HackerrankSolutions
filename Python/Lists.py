if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        operation, *attr = input().split()

        if operation == 'insert':
            index = int(attr[0])
            value = int(attr[1])
            list.insert(index, value)
        elif operation == 'remove':
            value = int(attr[0])
            list.remove(value)
        elif operation == 'append':
            value = int(attr[0])
            list.append(value)
        elif operation == 'sort':
            list.sort()
        elif operation == 'reverse':
            list.reverse()
        elif operation == 'pop':
            list.pop()
        elif operation == 'print':
            print(list)
