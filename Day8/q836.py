k = int(input())
x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]
p = 0
while k > 0:
    p += k
    if p % x1 == 0: k -= y1
    if p % x2 == 0: k -= y2
print(p)