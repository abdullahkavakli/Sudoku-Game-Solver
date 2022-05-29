global GRID
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
def suitable_for_number(coordinate,number_to_try):
    #zero and one comes from coordinate
    ith_block=coordinate[0]//3
    jth_block=coordinate[1]//3
    column = []; 
    for row in GRID: # transpose of the grid
        column.append(row[coordinate[1]])
    # Control for number existence in row, column and block
    return GRID[coordinate[0]].count(number_to_try)==0 and column.count(number_to_try)==0 and exist_in_block(ith_block,jth_block,number_to_try)==False  
def exist_in_block(ith_blok,jth_blok,number_to_try):
    ith_block_start=ith_blok*3
    jth_block_start=jth_blok*3 
    exist_flag=0
    for row in range(ith_block_start,ith_block_start+3):
        for column in range(jth_block_start,jth_block_start+3):
            if GRID[row][column]==number_to_try:
                exist_flag = 1
                break    
    return bool(exist_flag)    
def find_first_empty_place():
    for i in range(9):
        for j in range(9):
            if GRID[i][j]==0:
                return [i,j]
def place_number(coordinate,chosen_number):
    GRID[coordinate[0]][coordinate[1]]=chosen_number
    return True


def sudoku_solver():    
    coordinate_to_try=find_first_empty_place()
    if coordinate_to_try==None:
        return True
    for number_to_try in range(1,10):
        if suitable_for_number(coordinate_to_try,number_to_try)==True:
            place_number(coordinate_to_try,number_to_try)
            if sudoku_solver()==True:                    
                return True  
        GRID[coordinate_to_try[0]][coordinate_to_try[1]]=0           
    return False


def print_grid():
    for i in GRID:        
        print (i)
    print("\n")
    return True


def take_the_board_and_solve(new_board):
    global GRID
    GRID=new_board    
    sudoku_solver()
    return GRID
