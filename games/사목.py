from ast import Delete
from itertools import count
from tkinter import *
from venv import create
from functools import partial

window = None
frame1 = None

#전역변수
_MAXROW = 6
_MAXCOL = 7

bottomText = "새로 시작"

Turn = "빨강"                   # 순서

# 보드의 2중 배열
board = [[0 for i in range(_MAXCOL)] for j in range(_MAXROW)]

Col_count = [5 for i in range(_MAXCOL)]

cells = [[0 for i in range(_MAXCOL)] for j in range(_MAXROW)]

countNum = 0

def reset():
    global Turn, bottomText
    global board, Col_count, countNum
    global cells
    
    bottomText = "새로 시작"
    Turn = "빨강"
    board = [[0 for i in range(_MAXCOL)] for j in range(_MAXROW)]
    Col_count = [5 for i in range(_MAXCOL)]

    countNum = 0
    Bottom_Button.configure(text = bottomText)

    for r in range(_MAXROW):
        for c in range(_MAXCOL):
            cells[r][c].setColor("white")
            cells[r][c].setbgColor("blue")

# 셀 클래스
class Cell(Canvas):
    def __init__(self, parent, row, col, width = 20, height = 20):
        Canvas.__init__(self, parent, width = width, height = height,\
            bg = "blue", borderwidth = 2)
        

        self.color = "white"
        self.row = row
        self.col = col


        self.create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked, self.changeText)   # 버튼클릭시 클릭 멤버함수로

# 승리 예외처리
    def __checkVertical(self):      # 열방향 확인
        global bottomText, board, Turn, cells
        for i in range(_MAXROW):
            for j in range(_MAXCOL - 3):
                if (board[i][j] == board[i][j + 1] != 0):            # 첫번째 것과 다음 것이 색깔이 같다
                    if(board[i][j] == board[i][j + 2]):              # 첫번째 것과 2칸 앞이 같다
                        if(board[i][j] == board[i][j + 3]):          # 첫번째 것과 3칸 앞이 같다
                            if(board[i][j] == "빨강"):                    # 빨간색이 이겼다
                                bottomText = "Red Win!! 누르면 다시 시작"
                                cells[i][j].setbgColor("red")
                                cells[i][j + 1].setbgColor("red")
                                cells[i][j + 2].setbgColor("red")
                                cells[i][j + 3].setbgColor("red")
                            elif(board[i][j] == "노랑"):
                                bottomText = "Yellow Win!! 누르면 다시 시작"
                                cells[i][j].setbgColor("yellow")
                                cells[i][j + 1].setbgColor("yellow")
                                cells[i][j + 2].setbgColor("yellow")
                                cells[i][j + 3].setbgColor("yellow")
                            Bottom_Button.configure(text = bottomText)      # 밑에 글씨 바꿈
                            Turn = 0

    def __checkHorizontal(self):    # 행 방향 확인
        global bottomText, board, Turn, cells
        for i in range(_MAXROW - 3):
            for j in range(_MAXCOL):
                if (board[i][j] == board[i + 1][j] != 0):            # 첫번째 것과 다음 것이 색깔이 같다
                    if(board[i][j] == board[i + 2][j]):              # 첫번째 것과 2칸 앞이 같다
                        if(board[i][j] == board[i + 3][j]):          # 첫번째 것과 3칸 앞이 같다
                            if(board[i][j] == "빨강"):                    # 빨간색이 이겼다
                                bottomText = "Red Win!! 누르면 다시 시작"
                                cells[i][j].setbgColor("red")
                                cells[i + 1][j].setbgColor("red")
                                cells[i + 2][j].setbgColor("red")
                                cells[i + 3][j].setbgColor("red")
                            elif(board[i][j] == "노랑 누르면 다시 시작"):
                                bottomText = "Yellow Win!!"
                                cells[i][j].setbgColor("yellow")
                                cells[i + 1][j].setbgColor("yellow")
                                cells[i + 2][j].setbgColor("yellow")
                                cells[i + 3][j].setbgColor("yellow")
                            Bottom_Button.configure(text = bottomText)      # 밑에 글씨 바꿈
                            Turn = 0

    def __checkDiag1(self):         # 대각선 확인 1
        global bottomText, board, Turn, cells
        for i in range(_MAXROW - 3):
            for j in range(_MAXCOL - 3):
                if (board[i][j] == board[i + 1][j + 1] != 0):            # 첫번째 것과 다음 것이 색깔이 같다
                    if(board[i][j] == board[i + 2][j + 2]):              # 첫번째 것과 2칸 앞이 같다
                        if(board[i][j] == board[i + 3][j + 3]):          # 첫번째 것과 3칸 앞이 같다
                            if(board[i][j] == "빨강"):                    # 빨간색이 이겼다
                                bottomText = "Red Win!! 누르면 다시 시작"
                                cells[i][j].setbgColor("red")
                                cells[i + 1][j + 1].setbgColor("red")
                                cells[i + 2][j + 2].setbgColor("red")
                                cells[i + 3][j + 3].setbgColor("red")
                            elif(board[i][j] == "노랑"):
                                bottomText = "Yellow Win!! 누르면 다시 시작"
                                cells[i][j].setbgColor("yellow")
                                cells[i + 1][j + 1].setbgColor("yellow")
                                cells[i + 2][j + 2].setbgColor("yellow")
                                cells[i + 3][j + 3].setbgColor("yellow")
                            Bottom_Button.configure(text = bottomText)      # 밑에 글씨 바꿈
                            Turn = 0

    def __checkDiag2(self):         # 대각선 확인 2
        global bottomText, board, Turn
        for i in range(_MAXROW - 3, _MAXROW):
            for j in range(_MAXCOL - 3):
                if (board[i][j] == board[i - 1][j + 1] != 0):            # 첫번째 것과 다음 것이 색깔이 같다
                    if(board[i][j] == board[i - 2][j + 2]):              # 첫번째 것과 2칸 앞이 같다
                        if(board[i][j] == board[i - 3][j + 3]):          # 첫번째 것과 3칸 앞이 같다
                            if(board[i][j] == "빨강"):                    # 빨간색이 이겼다
                                bottomText = "Red Win!!"
                                cells[i][j].setbgColor("red 누르면 다시 시작")
                                cells[i - 1][j + 1].setbgColor("red")
                                cells[i - 2][j + 2].setbgColor("red")
                                cells[i - 3][j + 3].setbgColor("red")
                            elif(board[i][j] == "노랑"):
                                bottomText = "Yellow Win!! 누르면 다시 시작"
                                cells[i][j].setbgColor("yellow")
                                cells[i - 1][j + 1].setbgColor("yellow")
                                cells[i - 2][j + 2].setbgColor("yellow")
                                cells[i - 3][j + 3].setbgColor("yellow")
                            Bottom_Button.configure(text = bottomText)      # 밑에 글씨 바꿈
                            Turn = 0
    
    def __checkEnd(self):
        global countNum
        if(countNum == _MAXCOL * _MAXROW):
            bottomText = "No One Win..."
            Bottom_Button.configure(text= bottomText)

# 셀 클릭시 이벤트
    def clicked(self, event):
        global bottomText, Bottom_Button
        global Turn, Col_count
        global board, countNum
        if self.color == "white":
            if Col_count[self.col] == self.row:     # 값을 저장해서 밑에서부터 채워지게 함
                if Turn == "빨강":
                    nextcolor = "red"
                    Turn = "노랑"
                    board[self.row][self.col] = "빨강"               # 클릭하면 배열안의 숫자바뀜
                elif Turn == "노랑":
                    nextcolor = "yellow"
                    Turn = "빨강"
                    board[self.row][self.col] = "노랑"               # 클릭하면 배열안의 숫자바뀜
                else:
                    return
                countNum += 1
                Col_count[self.col] -= 1
                self.__checkVertical()                          # 돌이 놓이면 체크해본다.
                self.__checkHorizontal()
                self.__checkDiag1()
                self.__checkDiag2()
                self.__checkEnd()
            else:
                return
        else:
            return
        self.setColor(nextcolor)

# 클릭한 셀의 원 색 바꾸기
    def setColor(self, color):
        self.delete("oval")
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")

    def setbgColor(self, color):
        changeColor = color
        self.configure(bg=changeColor)

    def changeText(self):
        self.text.set(bottomText)

    def reset(self):
        self.color = "white"
        self.configure(bg="blue")


# 보드 함수
def create_board():

    global _MAXCOL, _MAXROW, window, Bottom_Button, cells

# 기본
    window = Tk()
    window.title("Connect Four")

#프레임
    frame1 = Frame(window)      #메인프레임
    frame1.pack()

#보드 생성
    for r in range(_MAXROW):
        for c in range(_MAXCOL):
            cells[r][c] = Cell(frame1, r, c, width = 20, height = 20)
            cells[r][c].grid(row= r, column= c)

   
# 밑에 프레임
    Bottom_frame = Frame(window, bg="white")
    Bottom_frame.pack()

    Bottom_Button = Button(Bottom_frame, padx=30, pady=5, text=bottomText, command=reset)
    Bottom_Button.pack()


# 


create_board()

window.mainloop()