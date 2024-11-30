N = int(input())


star_lst = [[' ']*(2*N-1) for _ in range(N)]

def Star(i, j, star_size):
    if star_size == 3 :
        star_lst[i][j] = '*'
        star_lst[i+1][j-1] = '*'
        star_lst[i+1][j+1] = '*'
        for k in range(-2, 3):
            star_lst[i+2][j+k] = '*'
    
    else:
        new_star_size = star_size//2
        Star(i,j,new_star_size)
        Star(i+new_star_size, j-new_star_size, new_star_size)
        Star(i+new_star_size, j+new_star_size, new_star_size)

Star(0, N-1, N)

for star in star_lst:
    print(''.join(star))