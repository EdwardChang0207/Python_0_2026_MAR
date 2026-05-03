t = int(input())
#重複t次
for i in range(t):#0 -> t-1
    #輸入一個數列
    l = input().split()
    for j in range(4):
        l[j] = int(l[j])
    #判斷是等差or等比
    if l[1]-l[0] == l[2]-l[1]: #等差
        a5 = l[3] + (l[1]-l[0])
    else:#等比
        a5 = l[3] * (l[1]//l[0])
    #計算5th
    #輸出
    for j in range(4):
        print(l[j], end=' ')
    print(a5)
'''
5 -> 你要處理五個數字
1 -> 1 / 3 = 0...1
2 -> 2 / 3 = 0...2
3 -> 3 / 3 = 1...0
4 -> 4 / 3 = 1...1
5 -> 5 / 3 = 1...2

0: 1
1: 2
2: 2
'''