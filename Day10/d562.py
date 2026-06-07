n = int(input())
l = input().split()
for _ in range(n):
    for i in range(len(l)):
        if i == len(l)-1:
            print(l[i])
        else:
            print(l[i],end=' ')
    l.pop(0)
    l.reverse()
