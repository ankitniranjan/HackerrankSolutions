# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
room = list(map(int, input().split()))

rooms = [0]*(len(room))
for i in room:
     rooms[i] += 1

print(rooms.index(1))
