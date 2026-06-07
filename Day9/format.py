'''
1.code & str
2.對齊
3.四捨五入取到小數後第幾位

windows xp, windows 7, windows vista
Linux

print('hi my name is', name[0], 'and I am', age[0],'years old.')
print('hi my name is', name[1], 'and I am', age[1],'years old.')
print('hi my name is', name[2], 'and I am', age[2],'years old.')

%s -> str
%d -> int
%f -> float
name = ['kevin', 'joe', 'alan']
age = [100, 8, 29]
print('hi my name is %5s and I am %3d years old' % (name[0], age[0]))
print('hi my name is {:5s} and I am {:3d} years old'.format(name[1], age[1]))
print(f'hi my name is {name[2]:5s} and I am {age[2]:3d} years old')
'''
pi = 3.1415926
print('%.2f' % pi)
print('{:.2f}'.format(pi))
print(f'{pi:.2f}')

'''
input: weight(kg), height(cm)
bmi = weight(kg)/height(m)**2
output:你的bmi是..(小數後兩位)，你的體重..
'''
w, h = [int(i) for i in input().split()]
h = h/100
bmi = w/h**2
if bmi < 18.5:
    r = '過輕'
elif bmi < 24:
    r = '剛好'
elif bmi < 27:
    r = '過重'
else:
    r = '肥胖'
print(f'你的bmi是{bmi:.2f},你的體重{r}')