#tic-tac-toe.py
###
### 
###
from tkinter import*
import tkinter.font
# Button에 패러매터를 주기 위한 모듈
from functools import partial
import tkinter

# 순서를 표시하는 전역함수. main에 있으면 계속 초기화되서 전역변수로 뺐음.
# 1 = o 차례, 2 = x 차례
turn = 1

# [도] 그림을 바꾸려면 game_board를 계속 불러야하는데, 함수 안에 있으면 초기화 돼서 전역변수로 만들었음.
button = []
    # 3 x 3 버튼에 따라 숫자를 변경시킬 이중 포문
    # 추가 : 보드에 값을 매겨 값에 따라 이미지가 바뀌도록 함
board = [[0 for x in range(3)] for y in range(3)]

# [도] 게임이 플레이중인가? -> bool 함수
isPlayGame = True


###함수
# 다음 놓을 차례

# 버튼 클릭시 순서 변경, 보드값 변경 함수
def change_button(i, j):
    global board, turn, isPlayGame

    if(isPlayGame):
        if(turn == 1):
            board[i][j] = 1
            turn = 2
            game_board()
        else:
            board[i][j] = 2
            turn = 1
            game_board()

# 게임판
def game_board():
    global board, button, turn, isPlayGame
  
    # 3 x 3 button을 그리는 포문
    if(isPlayGame):
        for i in range(3):
            m = i                
            button.append(i)
            button[i] = []
            for j in range(3):
                n = j
                button [i].append(j)
                # 추가 : 보드의 값에 따라 이미지 변경
                if(board[i][j] == 0):
                    button[i][j] = Button(root, image = i_empty ,  height = 90, width = 90, command=partial(change_button, i, j))   # 파라메터를 넘겨주기 위해 partial 사용
                elif(board[i][j] == 1):
                    button[i][j] = Button(root, image = i_o , height = 90, width = 90)
                elif(board[i][j] == 2):
                    button[i][j] = Button(root, image = i_x , height = 90, width = 90)
                button[i][j].grid(row=m, column=n)
        if(turn == 1):
            win_text = tkinter.Label(root, text = "o 차례", font = font)
            win_text.place( x=90, y = 295)
        else:
            win_text = tkinter.Label(root, text = "x 차례", font = font)
            win_text.place( x=90, y = 295)

    if(winner()):
        win_text = tkinter.Label(root, text = "      ", font = font)
        win_text.place( x=90, y = 295)
        print("게임이 끝났습니다.")
        isPlayGame = False
        if(turn == 1):
            win_text = tkinter.Label(root, text = "x win", font = font)
            win_text.place( x=90, y = 295)
        else:
            win_text = tkinter.Label(root, text = "o win", font = font)
            win_text.place( x=90, y = 295)


# 이겼는지 판단하는 함수
# ox 보드의 그림이 o 인지 x인지 넣어져 있는 변수.
def winner():
     return ((board[0][0] == board[0][1] == board[0][2] != 0) or
            (board[1][0] == board[1][1] == board[1][2] != 0) or
            (board[2][0] == board[2][1] == board[2][2] != 0) or
            (board[0][0] == board[1][0] == board[2][0] != 0) or
            (board[0][1] == board[1][1] == board[2][1] != 0) or
            (board[0][2] == board[1][2] == board[2][2] != 0) or
            (board[0][0] == board[1][1] == board[2][2] != 0) or
            (board[0][2] == board[1][1] == board[2][0] != 0))


#이미지 파일 3개 변수에 저장
def game_image():
    global i_empty
    global i_x
    global i_o
    i_empty = PhotoImage(file = "C:/develop/empty.gif")
    i_x = PhotoImage(file = "C:/develop/x.gif") 
    i_o = PhotoImage(file = "C:/develop/o.gif")



##############
def main():
##############
    #선언
    global root
    root = Tk()
    #사이즈
    root.geometry ("288x350+450+100")
    #타이틀
    root.title("TIC-TAC-TOC")
    #창크기 변환 X
    root.resizable(False, False )

   

    # 폰트
    global font
    font = tkinter.font.Font(family = "바탕체" , size = 30)
    #그림 넣기
    game_image()
    #보드 넣기
    game_board()

    root.mainloop()

    

 

main()