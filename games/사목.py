# import json
# import pprint

# jsonOb = json.loads(strJson)
# pprint.pprint(jsonOb)

# strJsonOb = json.dumps(jsonOb)
# print(strJsonOb)

from ast import Delete
from tkinter import *
from venv import create


window = None

#전역변수
_MAXROW = 6
_MAXCOL = 7

bottomText = "새로 시작"

Turn = "빨강"                   # 순서



# 보드의 2중 배열
board = [[0 for i in range(_MAXROW)] for j in range(_MAXCOL)]


Col_count = [5 for i in range(_MAXCOL)]


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
        pass

    def __checkHorizontal(self):    # 행 방향 확인
        pass

    def __checkDiag1(self):         # 대각선 확인 1
        pass

    def __checkDiag2(self):         # 대각선 확인 2
        pass

# 셀 클릭시 이벤트
    def clicked(self, event):
        global bottomText, Bottom_Button
        global Turn, Col_count
        if self.color == "white":
            if Col_count[self.col] == self.row:     # 값을 저장해서 밑에서부터 채워지게 함
                if Turn == "빨강":
                    nextcolor = "red"
                    Turn = "노랑"
                    bottomText = "Yellow turn"
                    board[self.row][self.col] = 1               # 클릭하면 배열안의 숫자바뀜
                    Bottom_Button.configure(text = bottomText)      # 밑에 글씨 바꿈
                elif Turn == "노랑":
                    nextcolor = "yellow"
                    Turn = "빨강"
                    bottomText = "Red turn"                  
                    board[self.row][self.col] = 2               # 클릭하면 배열안의 숫자바뀜
                    Bottom_Button.configure(text = bottomText)      # 밑에 글씨 바꿈
                Col_count[self.col] -= 1
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
    
    def changeText(self):
        self.text.set(bottomText)


# 보드 함수
def create_board():

    global _MAXCOL, _MAXROW, window, Bottom_Button

# 기본
    window = Tk()
    window.title("Connect Four")

#프레임
    frame1 = Frame(window)      #메인프레임
    frame1.pack()

#보드 생성
    for r in range(_MAXROW):
        for c in range(_MAXCOL):
            cell = Cell(frame1, r, c, width = 20, height = 20)
            cell.grid(row= r, column= c)

   
# 밑에 프레임
    Bottom_frame = Frame(window, bg="white")
    Bottom_frame.pack()

    Bottom_Button = Button(Bottom_frame, padx=30, pady=5, text=bottomText)
    Bottom_Button.pack()


# 


create_board()

window.mainloop()