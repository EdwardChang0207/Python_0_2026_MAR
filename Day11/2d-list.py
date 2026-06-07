l = [0, 1, 2, 3]
#game_map = [a, b, c]
game_map = [
    ['','',''],# a 0
    ['','',''],# b 1
    ['','','']#c 2
    # 0  1. 2
]
'''
input: 0 0

橫線(ROW)
'''
game = True
player = 'O'
while game:
    print(f"{player}'s turn")
    a, b = [int(i) for i in input().split()]
    if game_map[a][b]: continue
    game_map[a][b] = player

    for i in range(3):
        if game_map[i].count(player) == 3:
            print(f'{player} Won!')
            game = False
        
        col = [game_map[j][i] for j in range(3)]
        if col.count(player) == 3:
            print(f'{player} Won!')
            game = False

    l1 = [game_map[0][0], game_map[1][1], game_map[2][2]]
    l2 = [game_map[0][2], game_map[1][1], game_map[2][0]]

    for l in [l1, l2]:
        if l.count(player) == 3:
            print(f'{player} Won!')
            game = False

    if player == 'O': player = 'X'
    else: player = 'O'
    for i in game_map:
        print(i)