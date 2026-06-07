ans = 40
guess = -1
lower = 0
upper = 100
record = 0
#重複做猜的動作
while ans != guess:
    print(lower,'~',upper)
    guess = int(input())
    record += 1
    if guess < lower or guess > upper:
        print('error')
        continue
    if guess == ans:
        print('correct!', '你猜了', record, '次')
        break #結束遊戲
    elif guess > ans:
        print('too big!')
        upper = guess #修改上/下界
    else: #too small
        print('too small')
        lower = guess #修改上/下界
#記錄猜幾次