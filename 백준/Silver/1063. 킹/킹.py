# 1063_S3 킹

king_init, stone_init, N = input().split()

king_loc = []
stone_loc = []

# 킹의 움직임을 저장
king_move = []
for _ in range(int(N)):
    king_move.append(input())

dic_loc_y = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

dic_loc_x = {
    '8': 0,
    '7': 1,
    '6': 2,
    '5': 3,
    '4': 4,
    '3': 5,
    '2': 6,
    '1': 7
}

dic_loc_y_to_alpha = {
    '0': 'A',
    '1': 'B',
    '2': 'C',
    '3': 'D',
    '4': 'E',
    '5': 'F',
    '6': 'G',
    '7': 'H'
}

dic_loc_x_to_alpha = {
    '0': '8',
    '1': '7',
    '2': '6',
    '3': '5',
    '4': '4',
    '5': '3',
    '6': '2',
    '7': '1',                            
    
}

dic_move = {
    'R': [0, 1],
    'L': [0, -1],
    'B': [1, 0],
    'T': [-1, 0],
    'RT': [-1, 1],
    'LT': [-1, -1],        
    'RB': [1, 1],
    'LB': [1, -1]        
}

# king과 돌의 초기좌표
king_loc.append(dic_loc_x[king_init[1]]) # king 의 x좌표
king_loc.append(dic_loc_y[king_init[0]]) # king 의 y좌표

stone_loc.append(dic_loc_x[stone_init[1]]) # stone 의 x좌표
stone_loc.append(dic_loc_y[stone_init[0]]) # stone 의 y좌표

# king을 움직임
for i in king_move:
    nx_king = king_loc[0] + dic_move[i][0]
    ny_king = king_loc[1] + dic_move[i][1]
    
    # king이 좌표밖으로 나가면 없던일로    
    if nx_king<0 or nx_king>=8 or ny_king<0 or ny_king>=8:
        continue
    
    # 킹이 돌과 같은 곳으로 움직이면 돌을 같은방향으로 이동
    if nx_king == stone_loc[0] and ny_king == stone_loc[1]:
        nx_stone = stone_loc[0] + dic_move[i][0]
        ny_stone = stone_loc[1] + dic_move[i][1]
        
        #만약 stone이 좌표 밖으로 나가면 없던일로
        if nx_stone <0 or nx_stone >= 8 or ny_stone <0 or ny_stone >= 8:
            continue
            
        #아무 문제 없다면 stone의 좌표를 옮김
        stone_loc[0] = nx_stone
        stone_loc[1] = ny_stone    
            
    # 아무 문제 없다면 king의 좌표를 옮김        
    king_loc[0] = nx_king
    king_loc[1] = ny_king
    
print(''.join( [dic_loc_y_to_alpha[str(king_loc[1])], dic_loc_x_to_alpha[str(king_loc[0])]] ))
print(''.join( [dic_loc_y_to_alpha[str(stone_loc[1])], dic_loc_x_to_alpha[str(stone_loc[0])]] ))

