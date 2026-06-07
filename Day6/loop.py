'''
迴圈 loop

while <condiction:bool>:
    ...

i = 0
while i < 10:
    print(i)
    i = i + 1

1 2 4 8 16 32 64    

#O->O->O->O
l = ['鮭魚','鮪魚','玉子燒']

for sushi in l:
    print(sushi)
    if sushi == '鮭魚':
        print('拿')
s = 'hello'
for i in s:
    print(i)

range(start[init:0], end, interval[init:1])
start -> end-1 + interval
for i in range(10):
    print(i, end=' ')

0, ..., 9
9, ..., 0    
for i in range(9, -1, -1):
    print(i)

20 18 16 14 12 10 8 6 4 2 0    

for i in range(20, -1, -2):
    print(i)

continue(skip) break(stop)

20 / 3 = 6(商)...2(餘)
i % 3 == 0 ?
9 / 3 = 3...0
19 / 4 = 4...3
19 % 4 = 3
for i in range(10):
    if i % 3 == 0: continue#如果遇到3的倍數就跳過
    if i == 8: break
    print(i)

l = [i for i in range(10)]
print(l)

a = ['123','456','789']
l = [int(i) for i in a]
print(l)

l = [int(i) for i in input().split()]
print(l)
#input -> int
#'10 20 30'-> ['10','20','30'] -> [10, 20, 30]
'''

l = [i for i in range(10) if i % 3 != 0]
print(l)