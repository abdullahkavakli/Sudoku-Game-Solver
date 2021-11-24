GRID = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


def sayi_icin_yer_münasip_mi(koordinat,sayımız):

    ith_blok=koordinat[0]//3
    jth_blok=koordinat[1]//3

    column = [];        # empty list
    for row in GRID:
        column.append(row[koordinat[1]])

    if GRID[koordinat[0]].count(sayımız)==0 and column.count(sayımız)==0 and (blokta_o_sayı_var_mı(ith_blok,jth_blok,sayımız)==False): 
        return True
    else:
        return False

    
def blokta_o_sayı_var_mı(ith_blok,jth_blok,sayımız):

    ith_blok_başlangıcı=ith_blok*3
    jth_blok_başlangıcı=jth_blok*3 

    flag=0
    for satır in range(ith_blok_başlangıcı,ith_blok_başlangıcı+3):
        for sütun in range(jth_blok_başlangıcı,jth_blok_başlangıcı+3):
            if GRID[satır][sütun]==sayımız:
                flag = 1
                break
    
    if flag==1:
        return True

    return False


def ilk_bos_yeri_bul():

    for i in range(9):
        for j in range(9):
            if GRID[i][j]==0:
                return [i,j]



def o_sayıyı_yerine_koy(koordinat,sayi):
    GRID[koordinat[0]][koordinat[1]]=sayi
    return True


def sudoku_solver():    
    denencek_koordinat=ilk_bos_yeri_bul()
    if denencek_koordinat==None:
        return True
    for sayi in range(1,10):
        if sayi_icin_yer_münasip_mi(denencek_koordinat,sayi)==True:
            o_sayıyı_yerine_koy(denencek_koordinat,sayi)
            if sudoku_solver()==True:                    
                return True            
            #else:
        GRID[denencek_koordinat[0]][denencek_koordinat[1]]=0           
    return False


def yazdır():
    for i in GRID:        
        print (i)
    print("\n")
    return True

#yazdır()
#sudoku_solver()
#yazdır()


def take_the_board_and_solve(new_board):
    global GRID
    GRID=new_board    
    sudoku_solver()
    return GRID
