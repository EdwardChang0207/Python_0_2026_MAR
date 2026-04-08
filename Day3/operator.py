'''
1.math num op num -> num
    (1)+ 加法 addition
    (2)- 減法 subtraction
    (3)* 乘法 multiplication
    (4)/ 除法 division
    (5)// 整除(商數) floor division
    (6)% 取餘數 modulus
    (7)** 次方(指數) exponentiation   
    10 / 3 = 3(商)...1（餘）
2.關係運算子 comparison operator num op num -> bool
    (1) == 等於 equal to
    (2) != 不等於 not equal to
    (3) > 大於 greater than
    (4) < 小於 less than
    (5) >= 大於等於 greater than or equal to
    (6) <= 小於等於 less than or equal to
3.邏輯運算子 logical operator bool op bool -> bool
    (1) not 反閘
        周杰倫：哎呦不錯喔 -> True
        不(not)錯(False) -> True
        錯 -> False
        不(not)行(True) -> False
        行 -> True
    (2) or 或閘
        math or english -> 3000
        T       F           T
        F       T           T
        T       T           T
        F       F           F(真值表 truth table)
    (3) and 且閘
        功課 and 打掃 -> :)
        T        F.     F
        F.       T.     F
        T        T.     T
        F.       F.     F
    (4) xor excursive or 斥或閘
        珍奶 xor 烏龍 -> :)
        T.       F.     T
        F.       T.     T
        T.       T.     F
        F.       F.     F 
        [1] and or not
            whitelist (a or b)
            blacklist (a and b)
            whitelist and blacklist
            (a or b) and not(a and b) -> xor
        [2] binary
'''

a, b = False, False
print(a or b)
print(a and b)
print((a or b) and not(a and b)) 