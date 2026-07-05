n = int(input())
l = [int(i) for i in input().split()]

max_n = max(l)
min_n = min(l)
max_i = l.index(max_n)
min_i = l.index(min_n)

print(max_n, max_i+1)
print(min_n, min_i+1)