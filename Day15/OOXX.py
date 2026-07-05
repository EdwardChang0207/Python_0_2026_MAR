game_map = [
    ['','',''], #0
    ['','',''], #1
    ['','','']  #2
     #0 #1 #2
]
game = True
player = 'O'
while game:
    print(f"{player}'s turn")
    a, b = [int(i) for i in input().split()]
    if game_map[a][b]: 
        print('error')
        continue
    game_map[a][b] = player
    print(*game_map, sep='\n')

    for i in range(3):
        if game_map[i].count(player) == 3:
            print(f'{player} Won')
            game = False
        col = [game_map[j][i] for j in range(3)]
        if col.count(player) == 3:
            print(f'{player} Won')
            game = False

    l1 = [game_map[i][i] for i in range(3)]
    l2 = [game_map[i][2-i] for i in range(3)]
    for l in [l1, l2]:
        if l.count(player) == 3:
            print(f'{player} Won')
            game = False

    if player == 'O': player = 'X'
    else: player = 'O'