
import pygame
from sys import exit
import numpy as np
import time
from  sudokusolver import take_the_board_and_solve
import copy
try:
    import dbconnection
except:
    pass    


class Grid:
    global board
    global board_immutable
    global board_temp
    global boardsolved
    global board_default

    board_default=[
        [7,4,0,0,0,0,0,3,0],
        [6,8,0,0,0,0,5,0,0],
        [9,0,0,0,0,0,0,0,8],
        [8,0,0,5,0,0,0,0,9],
        [0,0,0,0,0,0,0,0,2],
        [0,3,4,0,7,1,0,5,0],
        [0,0,0,0,4,0,1,0,0],
        [0,2,0,8,0,7,9,6,0],
        [0,7,6,0,0,2,0,0,3]
    ]    

    try:
        board=dbconnection.choose_random()
    except:
        board=board_default
        # If you want to test you can uncomment this:
        # board = [
        # [7, 4, 5, 2, 8, 9, 6, 3, 1],
        # [6, 8, 2, 7, 1, 3, 5, 9, 4],
        # [9, 1, 3, 4, 5, 6, 2, 7, 8],
        # [8, 6, 7, 5, 2, 4, 3, 1, 9],
        # [1, 5, 9, 3, 6, 8, 7, 4, 2],
        # [2, 3, 4, 9, 7, 1, 8, 5, 6],
        # [3, 9, 8, 6, 4, 5, 1, 2, 7],
        # [4, 2, 1, 8, 3, 7, 9, 6, 5],
        # [5, 7, 6, 1, 9, 2, 4, 8,0]
        # ]

    board_immutable = copy.deepcopy(board)
    board_temp =copy.deepcopy( board)
    boardsolved=copy.deepcopy(board)
    boardsolved= take_the_board_and_solve(boardsolved) 

    @staticmethod
    def initialize_again():
        global board
        global board_immutable
        global board_temp
        global boardsolved
        global board_default

        board_default=[
            [7,4,0,0,0,0,0,3,0],
            [6,8,0,0,0,0,5,0,0],
            [9,0,0,0,0,0,0,0,8],
            [8,0,0,5,0,0,0,0,9],
            [0,0,0,0,0,0,0,0,2],
            [0,3,4,0,7,1,0,5,0],
            [0,0,0,0,4,0,1,0,0],
            [0,2,0,8,0,7,9,6,0],
            [0,7,6,0,0,2,0,0,3]
        ]    

        try:
            board=copy.deepcopy(dbconnection.choose_random())
        except:
            board=copy.deepcopy(board_default)
            # If you want to test you can uncomment this:
            # board = [
            # [7, 4, 5, 2, 8, 9, 6, 3, 1],
            # [6, 8, 2, 7, 1, 3, 5, 9, 4],
            # [9, 1, 3, 4, 5, 6, 2, 7, 8],
            # [8, 6, 7, 5, 2, 4, 3, 1, 9],
            # [1, 5, 9, 3, 6, 8, 7, 4, 2],
            # [2, 3, 4, 9, 7, 1, 8, 5, 6],
            # [3, 9, 8, 6, 4, 5, 1, 2, 7],
            # [4, 2, 1, 8, 3, 7, 9, 6, 5],
            # [5, 7, 6, 1, 9, 2, 4, 8,0]
            # ]

        board_immutable = copy.deepcopy(board)
        board_temp =copy.deepcopy( board)
        boardsolved=copy.deepcopy(board)
        boardsolved= take_the_board_and_solve(copy.deepcopy(boardsolved)) 

   

class Visualizer:

    def available_for_number(self,koordinat,number):

        ith_blok=koordinat[0]//3
        jth_blok=koordinat[1]//3

        column = []; 
        for row in board_temp:
            column.append(row[koordinat[1]])



        if board_temp[koordinat[0]].count(number)==0 and column.count(number)==0 and (self.is_there_a_number_in_that_block(ith_blok,jth_blok,number)==False): 
            return True
        else:
            return False
        
    def is_there_a_number_in_that_block(self,ith_blok,jth_blok,sayımız):

        ith_block_beginning=ith_blok*3
        jth_block_beginning=jth_blok*3 

        flag=0
        for satır in range(ith_block_beginning,ith_block_beginning+3):
            for sütun in range(jth_block_beginning,jth_block_beginning+3):
                if board_temp[satır][sütun]==sayımız:
                    flag = 1
                    break
        
        if flag==1:
            return True

        return False

    def find_first_available_place(self):

        for i in range(9):
            for j in range(9):
                if board[i][j]==0:
                    return [i,j]

    def put_into_place(self,koordinat,sayi):
        board[koordinat[0]][koordinat[1]]=sayi
        return True

    def sudoku_solver(self):    
        denencek_koordinat=self.find_first_available_place()
        if denencek_koordinat==None:
            return True
        for sayi in range(1,10):
            if self.available_for_number(denencek_koordinat,sayi)==True:
                self.put_into_place(denencek_koordinat,sayi)
                if self.sudoku_solver()==True:                    
                    return True   
            board[denencek_koordinat[0]][denencek_koordinat[1]]=0           
        return False

    def sudoku_solver_visualizer(self):    
        coordinate_to_try=self.find_first_available_place()
        if coordinate_to_try!=None:
            x,y=coordinate_to_try     
            # time.sleep(0.0001)
        
        if coordinate_to_try==None:
            return True
        
        for sayi in range(1,10):
                        
            #time.sleep(0.1)
            if self.available_for_number(coordinate_to_try,sayi)==True:
                self.put_into_place(coordinate_to_try,sayi)
                Square_matrix[x][y].deger=sayi
                board[x][y]=sayi
                Square_matrix[x][y].set_green()

                square_group.draw(screen)
                square_group.update()
                pygame.display.update()
                
                
                for i in range(len(board)):
                    for j in range(len(board)):
                        board_temp[i][j]=board[i][j]
                #time.sleep(1)

                if self.sudoku_solver_visualizer()==True:                    
                    return True   
            board[coordinate_to_try[0]][coordinate_to_try[1]]=0
            board_temp[coordinate_to_try[0]][coordinate_to_try[1]]=0
            Square_matrix[coordinate_to_try[0]][coordinate_to_try[1]].set_red()
            
        return False


class Kare(pygame.sprite.Sprite):


    def __init__(self,i,j):
        super().__init__()
        pygame.font.init()
        self.x_ind=i
        self.y_ind=j
        self.surface=pygame.Surface((70,70))
        self.surface.fill('White')
        self.image=self.surface

        if self.x_ind//3==0:
            self.equivalent_x=i*71+10
        elif  self.x_ind//3==1:
            self.equivalent_x=i*71+12
        elif self.x_ind//3==2:
            self.equivalent_x=i*71+14


        if self.y_ind//3==0:
            self.equivalent_y=j*71+10
        elif self.y_ind//3==1:
            self.equivalent_y=j*71+12
        elif self.y_ind//3==2:
            self.equivalent_y=j*71+14


        self.rect=self.surface.get_rect(topleft=(self.equivalent_y,self.equivalent_x))
        self.rect_for_collide=self.rect
        self.mouse=0
        self.number_in_matrix=board[self.x_ind][self.y_ind] 
        self.game_message = square_font.render(str(board[self.x_ind][self.y_ind]) ,False,(111,196,169))

    def update(self):	    
        self.deger=board[self.x_ind][self.y_ind]
        self.game_message = square_font.render(str(self.deger) ,True,(0,50,0))
        self.game_message_rect = self.game_message.get_rect(center=self.rect_for_collide.center)
        if self.deger!=0:        
            screen.blit(self.game_message,self.game_message_rect)
        

    def get_mouse(self):
        return self.mouse

    def set_mouse(self,int):
        self.mouse=int
        pass

    def set_red(self):
        self.surface=pygame.Surface((70,70))
        self.surface.fill('Red')
        self.image=self.surface
        self.update()

    def set_green(self):
        self.surface=pygame.Surface((70,70))
        self.surface.fill('Green')
        self.image=self.surface
        
    def set_white(self):
        self.surface=pygame.Surface((70,70))
        self.surface.fill('White')
        self.image=self.surface
        

# def main():

pygame.init()
screen = pygame.display.set_mode((660,660))
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()

square_font=pygame.font.Font(None,50)
font_congrats=pygame.font.Font(None,100)
        

game_active=True

Square_matrix=[ [ 0 for i in range(9) ] for j in range(9) ]

square_group=pygame.sprite.Group()

Visualize=Visualizer()

for i in range(9):
    for j in range(9):
        eklenecek=Kare(i,j)
        square_group.add(eklenecek)
        Square_matrix[i][j]=eklenecek

def check_index(): 
    for i in range(9):
        for j in range(9):
            if Square_matrix[i][j].get_mouse()==1:                
                return i,j
    return None


def set_all_white(): 
    for i in range(9):
        for j in range(9):
            Square_matrix[i][j].set_white()            
    return None


while True:
        if game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    for i in range(9):
                        for j in range(9):  
                            Square_matrix[i][j].set_mouse(0)                      
                            if Square_matrix[i][j].rect.collidepoint(x,y):
                                Square_matrix[i][j].set_mouse(1)
                    
                if event.type == pygame.KEYDOWN :

                
                    if (event.key >47 and event.key<58) :                    
                        coordinates_to_changed=check_index() 
                        
                        if (coordinates_to_changed!=None):                             
                            x,y=coordinates_to_changed
                            changed_number=event.key-48
                            Square_matrix[x][y].deger=changed_number
                            board[x][y]=changed_number
                        

                    elif (event.key >1073741912 and event.key<1073741922):
                        coordinates_to_changed=check_index()                 
                        
                        if (coordinates_to_changed!=None):
                            x,y=coordinates_to_changed
                            changed_number=event.key-1073741912
                            Square_matrix[x][y].deger=changed_number
                            board[x][y]=changed_number
                            
                    elif event.key==1073741922:# for number 0 in rhs    
                        coordinates_to_changed=check_index()                  
                        
                        if (coordinates_to_changed!=None):                         
                            x,y=coordinates_to_changed
                            changed_number=0
                            Square_matrix[x][y].deger=changed_number
                            board[x][y]=changed_number
                
                    elif event.key==pygame.K_SPACE:
                        game_active=False
                        break

                    
                    
        if game_active==False :
            board=board_immutable
            Visualize.sudoku_solver_visualizer()

            print("New game is starting...")

            time.sleep(4) 
            
            set_all_white()       
            sample_surface = pygame.display.set_mode((660,660))
            Grid.initialize_again()
            square_group.update()
            pygame.display.update()            
             
            game_active=True    
            print("")               

        if(boardsolved==board and game_active==True)    :        
            
            game_name = font_congrats.render('Congratulations!!',False,(0,153,0))
            game_name_rect = game_name.get_rect(topleft = (40,40))
            screen.blit(game_name,game_name_rect)
            
            pygame.display.update()
            time.sleep(4)            
        
            sample_surface = pygame.display.set_mode((660,660))

            pygame.display.update()
            square_group.update()
            print("New game is starting...")
            Grid.initialize_again()
            

        
        square_group.draw(screen)
        square_group.update()
        pygame.display.update()
        
        clock.tick(1)

