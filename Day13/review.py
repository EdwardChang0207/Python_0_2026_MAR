'''
#Input(原料)/Output(結果)
print(123)
print(456+123)
print('abc') #讓他照抄 -> ''/"" (人類的語言->字串 string -> str)
print(123, 'abc', 123+456, 'hi')#, -> 分隔
print(123, 'abc', 123+456, 'hi', sep='@', end=' ')#分隔符號 seprate -> sep(init:空格)
print('hello')#結尾符號 end (init:'\n' 換行)

print(input('請輸入姓名')) #烤箱
#split('切割符號(init:空格)') -> 分割
#. -> 1.的 ＊2.對...做...
input().split() #'10 20' -> ['10', '20']
#變數 variable -> 箱子
name = input('請輸入姓名')
print(name)

#input:name, output:hi, [name]
name = input('請輸入姓名')
print('hi,', name)

name, age = input('請輸入姓名'), input('請輸入年齡')
print('my name is', name, 'and I am', age, 'years old.')

1.不可用數字當開頭
    a1 = 1 # (V)
    1a = 1 # (X)
2.不可用保留字
    print = 1 #(X)
3.兩個以上的單字
    username = 'alan'
    userName = 'alan'
    user_name = 'alan'
    user_Name = 'alan' (很少人用)
4.不會改變的內容 -> 常數
    PI = 3.1415926

資料型態
1.Numbers
    (1)整數 integer -> int: 沒有小數點的數
    (2)浮點數 float: 有小數點的數
    eg. 1(int), -1(int), pi(float), 3.0(float)
2.Text
    (1)字串 string -> str: ''/""
3.Boolean
    (1)True -> 1
    (2)False -> 0
4.List
    (1)串列 list:存多個資料
        l = [123, 'hello', True, 123+456]
        #.    0.     1.      2.     3
        print(l[2])

type() -> 得到資料型態
a = input()
print(type(a))

float -> int 無條件捨去
    a = 3.14
    print(int(a))
    -> 3

str -> int 字串內的內容一定要是整數
    (X)
    a = '3.14'
    print(int(a))
    (V)
    a = '3'
    print(int(a))

bool -> int
    True -> 1
    False -> 0
    print(int(True))
    print(int(False))

list -> int (X)

int -> float 後面.0
    a = 3
    print(float(a))
    -> 3.0

str -> float 字串裡面要是浮點數/整數
    a = '3.14'
    print(float(a))
    ->3.14

運算子 Operator
1.Math num op num -> num
    int op int -> int (例外: / -> float)
    int op float -> float
    float op float -> op 
    (1)+ 加
        print(5+8)
    (2)- 減
        print(20-7)
    (3)* 乘
        print(3*9)
    (4)/ 除
        print(20/7)
    (5)% 取餘數
        print(30%8)
    (6)// 取商數
        print(27//5)
    (7)** 指數（次方）
        print(5**3)

2.關係 num op num -> bool
    (1)> 大於
        print(2>1)  
    (2)< 小於
        print(10<3)
    (3)>= 大於等於
        print(5>=2)
    (4)<= 小於等於
        print(10<=10)
    (5)== 相等
        print(1==1)
    (6)!= 不相等 # ! -> 相反
        print(2!=1)
    (7)in 在裡面
        l = [1, 2, 3, 4]
        print(2 in l)

3.Logic bool op bool -> bool
    (1)not 反閘
        周杰倫：哎呦不錯喔
        不(not)錯 -> True
        錯 -> False
        不(not)行 -> False
        行 -> True
        print(not True)
        print(not False)
    (2)or 或閘
        math or english -> 3000
        T.         F.      T
        F.         T.      T
        T.         T.      T
        F.         F.      F (真值表 truth table)
        a, b = False, False
        print(a or b)
    (3)and 且閘
        HW and 打掃 -> :)
        T.     F.      F
        F.     T.      F
        T.     T.      T
        F.     F.      F
        a, b = False, False
        print(a and b)
    (4)xor (excursive or) 斥或閘
        珍奶 xor 烏龍 -> :)
        T.       F.     T
        F.       T.     T
        T.       T.     F
        F.       F.     F

        [1]and or not
            a, b = False, False
            print((a or b) and not(a and b))
        [2]binary
            a, b = False, False
            print(a^b)
4.String & List
    1.+
        print('abc'+'efg')
        print([1,2,3]+[4,5,6])
    2.*
        print('abc'*2)
        print([1,2,3]*3)
            
1. print(True or False, 1+123, 'hello', sep='!')
    -> True!124!hello
2. print(not(True) or not(False))
    -> True
3. input() -> datatype = ?
    -> String
4. print(not(True or False) and False)
    -> True or False -> True
    -> not(True) and False
    -> False and False
    -> False
5. (a or b) and not(a and b) == a^b
    -> True/False
    a, b = 1, 5
    print(((a or b) and not(a and b)) == (a^b))
6. print('abc'*3 + 'cde')
    ->abcabcabccde
7. print([0]*3 + [1,2,3]*2)
    ->[0,0,0,1,2,3,1,2,3]
8. print(int(3.14)+float(3)+int(True))  
    ->3+3.0+1
    ->7.0
9. print(int(3.14) + float(False) * 3.1)
    -> 3 + 0.0 * 3.1
    -> 3 + 0.0
    -> 3.0
10. print(23 // (float(True)+1))
    -> 23 // 2.0
    -> 11.0

格式化
1.解決字串跟變數混合輸出
2.取到小數後第幾位

eg.Hi, my name is [name], and I am [age] years old.

格式符號：%s -> str, %d -> int, %f -> float
%[num]s -> 至少要有num格 == 至少輸出num個字元
name, age = ['alan','kevin','kai'],  [8, 20, 100]
# (1)%
print('Hi, my name is %-5s, and I am %3d years old.' % (name[0], age[0]))
# (2).format
print('Hi, my name is {:5s}, and I am {:3d} years old.'.format(name[1], age[1]))
# (3)f-string
print(f'Hi, my name is {name[2]:5s}, and I am {age[2]:3d} years old.')

pi = 3.1415926
print('pi = %5.2f' % pi)
print('pi = {:5.2f}'.format(pi))
print(f'pi = {pi:5.2f}')

條件
if <condiction:bool>:
    ...
if [天氣好]: 
[TAB]去打球
elif 心情好:
    打電動
elif ...
else:
    在家睡覺
# (1)
if 1 < 2: print('hi')
elif 1 == 1: print('hello')
else: print(123)

# (2)
if 1 < 2: print('hi')
if 1 == 1: print('hello')
else: print(123)

迴圈

1.whlie
while <bool>:
    ...
idx = 1
r = 1
while idx <= 10:
    print(f'r:{r}, idx:{idx}')
    r += idx
    idx += 1

#1,2,3,...,10
#1,3,5,7,...,21
#100, 99, 98,...., 60
#1, 2, 4, 8, 16, 32, 64, ..., 1024
#1, 2, 4, 7, 11, 16, 22, 29, 37, 46

2.for
l = ['a', 'b', 'c']
for i in l:
    print(i)
sushi = ['鮭魚','鮪魚','玉子燒']
for i in sushi:
    print(f'現在經過的是：{i}')
    if i == '鮭魚':
        print(f'拿{i}')

s = 'hello'
for i in s:
    print(i)

range(start[init:0], end, interval[inti:1])
from start -> end-1, += interval
    
for i in range(0, 10, 1):
    print(i, end=' ')
print()
for i in range(0, 10, 2):
    print(i, end=' ')
for i in range(0, 10):
    print(i, end=' ')
print()
for i in range(10):
    print(i, end=' ')

l = [i for i in range(1, 11)]
print(l)
#10 -> 1
l = [i for i in range(10, 0, -1)]
print(l)

#10 20
a, b = [int(i) for i in input().split()]
print(a,b)
l = [i**2 for i in range(10, 0, -1)]
print(l)
l = [0 for _ in range(10)]
print(l)

continue, break
for i in range(10):
    if i % 3 == 0: continue
    if i == 8: break
    print(i, end=' ')
l = []
if l: print('hello')
else: print(123)

#l[start(init:0):end(init:-1):interval(init:1)]
l = [i for i in range(10)]
print(l[1:4:1])
l = [i for i in range(10)]
print(l[-1])

l = [i for i in range(10)]
print(len(l)) #len -> length
print(max(l)) #max -> maximum
print(min(l)) #min -> minimum
print(sum(l)) #總和

l = []
for i in range(10):
    l.append(i) #新增
print(l)
l.append(0)
l.append(0)
l.append(0)
a = l.pop(2) #拿出
print(f'a:{a}, l:{l}')
l.insert(2, 10)
print(l)
l.remove(10)
print(l)
l.reverse()
print(l)
l.sort()
print(l)
a = l.index(8)
print(f'8在{a}號位置')
print(f'l裡面有{l.count(0)}個0')
'''