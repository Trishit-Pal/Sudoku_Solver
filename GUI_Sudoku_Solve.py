import pygame
import time
from Solver import solve_grid, check_valid, search_blank
pygame.font.init()


class Sudoku_Grid:
    sudoku_grid = [
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

    def __init__(self,rows,cols,width,height):
        self.rows=rows
        self.cols=cols
        self.cubes=[[Cube(self.sudoku_grid[i][j],i,j,width,height) for j in range(cols)] for i in range(rows)]
        self.width=width
        self.height=height
        self.model=None
        self.selected = None

    def update_model(self):
        self.model=[[self.cubes[i][j].val for j in range(self.cols)]for i in range(self.rows)]
    
    def place(self,v):
        row,col=self.selected
        if (self.cubes[row][col].val==0):
            self.cubes[row][col].set(v)
            self.update_model()

            if check_valid(self.model,v,(row,col)) and solve_grid(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self,v):
        row,col=self.selected
        self.cubes[row][col].set_temp(v)

    def draw(self,win): #drawing grid lines
        gap=self.width/9
        for i in range(self.rows+1):
            if (i % 3 == 0 and i !=0):
                thick=4
            else:
                thick=1
            pygame.draw.line(win,(0,0,0), (0,i*gap), (self.width,i*gap),thick)
            pygame.draw.line(win, (0, 0, 0), (i* gap,0), (i * gap,self.height), thick)

        #Drawing Cubical Boxes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self,row,col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected=False
        self.cubes[row][col].selected=True
        self.selected=(row,col)
 
    def clear(self): #holds value temporarily in the box when typed through keyboard else sets it to blank ot zero
        row,col=self.selected
        if (self.cubes[row][col].val==0):
            self.cubes[row][col].set_temp(0)

    def click(self,pos):
        if ((pos[0]<self.width) and (pos[1]< self.height)):
            gap=self.width /9
            x=pos[0]//gap
            y=pos[1]//gap
            return (int(y),int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].val==0:
                    return False
        return True

    

    
class Cube:
    rows=9
    cols=9

    def __init__(self,val,row,col,width,height):
        self.val=val
        self.temp=0
        self.row=row
        self.col=col
        self.width= width
        self.height=height
        self.selected=False

    def draw(self,win):
        fnt=pygame.font.SysFont("comicsans",40)
        gap=self.width /9
        x=self.col *gap
        y=self.row *gap

        if self.temp !=0 and self.val==0:
            text=fnt.render(str(self.temp),1,(128,128,128))
            win.blit(text,(x+5,y+5))
        elif not(self.val==0):
            text=fnt.render(str(self.val),1,(0,0,0))
            win.blit(text,(x+(gap/2 - text.get_width()/2), y+(gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win,(255,0,0),(x,y,gap,gap),3)


    def set(self,val):
        self.val=val

    def set_temp(self, val):
        self.temp = val    



def redraw_window(win, board, time, strikes):
        win.fill((255, 255, 255))
        # Draw time
        fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render("Time:" + format(time), 1, (0, 0, 0))
        win.blit(text, (540 - 160, 560))
        # Draw Strikes
        text = fnt.render("X " * strikes, 1, (255, 0, 0))
        win.blit(text, (20, 560))
        # Draw grid and board
        board.draw(win)

def format(seconds):
        sec=seconds%60
        min=seconds//60
        hr=min//60

        res=" " + str(min) + ":" + str(sec)
        return res

def main():
        win=pygame.display.set_mode((540,600))
        pygame.display.set_caption("Sudoku Solver")
        sudoku_grid=Sudoku_Grid(9,9,540,540)
        key=None
        run=True
        start=time.time()
        strikes=0
        while run:
            play_time=round(time.time()-start)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_1:
                        key=1
                    if event.key== pygame.K_2:
                        key=2
                    if event.key== pygame.K_3:
                        key=3
                    if event.key== pygame.K_4:
                        key=4
                    if event.key== pygame.K_5:
                        key=5
                    if event.key== pygame.K_6:
                        key=6
                    if event.key== pygame.K_7:
                        key=7
                    if event.key== pygame.K_8:
                        key=8
                    if event.key== pygame.K_9:
                        key=9                   
                    if event.key==pygame.K_DELETE:
                        sudoku_grid.clear()
                        key=None
                    if event.key == pygame.K_RETURN:
                        i, j = sudoku_grid.selected
                        if sudoku_grid.cubes[i][j].temp != 0:
                            if sudoku_grid.place(sudoku_grid.cubes[i][j].temp):
                                print("Correct!")
                            else:
                                print("Wrong!!")
                                strikes += 1
                            key = None

                            if sudoku_grid.is_finished():
                                print("Congartulations! Game over !!")
                                run=False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked = sudoku_grid.click(pos)
                    if clicked:
                        sudoku_grid.select(clicked[0], clicked[1])
                        key = None

            if sudoku_grid.selected and key != None:
                    sudoku_grid.sketch(key)

            redraw_window(win, sudoku_grid, play_time, strikes)
            pygame.display.update()

main()
pygame.quit()

