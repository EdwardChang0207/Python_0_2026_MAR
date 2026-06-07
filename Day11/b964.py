n = int(input())
s = [int(i) for i in input().split()]

#排序
s.sort()
#輸出
for i in range(n):
    if i == n-1:
        print(s[i])
    else:
        print(s[i],end=' ')
#best case
if s[0] >= 60:
    print('best case')
    print(s[0])#及格最低分
#worst case
elif s[-1] < 60:
    print(s[-1])#不及格最高分
    print('worst case')
#normal case
#-------b|60|a------
else:
    for i in range(n):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])
            break