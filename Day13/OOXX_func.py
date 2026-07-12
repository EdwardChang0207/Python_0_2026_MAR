def error_detect(game_map, a, b):
    result = bool(game_map[a][b])
    return result

def winner_detect(game_map, player):
    for i in range(3):
        if game_map[i].count(player) == 3:
            print(f'{player} won!')
            return False
        col = [game_map[j][i] for j in range(3)]
        if col.count(player) == 3:
            print(f'{player} won!')
            return False
    l1 = [game_map[i][i] for i in range(3)]
    l2 = [game_map[i][2-i] for i in range(3)]
    for i in [l1,l2]:
        if i.count(player) == 3:
            print(f'{player} won!')
            return False
    return True

def player_change(player):
    if player == 'O': return 'X'
    else: return 'O'

def show_gamemap(game_map):
    for i in game_map:
        print(i)

game_map = [
    ['','',''],
    ['','',''],
    ['','','']
]
game = True
player = 'O'
while game:
    show_gamemap(game_map)
    a, b = [int(i) for i in input().split()]
    if error_detect(game_map, a, b): 
        print('error')
        continue
    game_map[a][b] = player
    game = winner_detect(game_map, player)
    player = player_change(player)
