import math
from tkinter import * # Import tkinter
from random import randint
    
class Hangman:
    hiddenWord, guessWord, nMissedLetters = [], [], []    # 파일에서 찾은 단어, 맞추고 있는 단어, 틀린 단어 리스트
    nCorrectChar, nMissChar = 0, 7                          # 맞춘 개수, 틀린 개수
    finished = 0                                            # 0 = 아직 안 끝남, 1 = 맞춤, 2 = 틀림

    def __init__(self, words):
        self.hiddenWord = words
        # print(self.hiddenWord)
        self.draw()

    def draw(self):
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        canvas.delete("hangman")

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger
        
        radius = 20 # 반지름
        
        if(self.nMissChar >= 1):                                    # 줄
            canvas.create_line(160, 20, 160, 40, tags = "hangman")  # Draw the hanger

        if(self.nMissChar >= 2):                                    # 머리
        # Draw the circle
            canvas.create_oval(140, 40, 180, 80, tags = "hangman")  # Draw the hanger

        if(self.nMissChar >= 3):                                    # 왼쪽 팔
        # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
            x1 = 160 - radius * math.cos(math.radians(45))
            y1 = 60 + radius * math.sin(math.radians(45))
            x2 = 160 - (radius+60) * math.cos(math.radians(45))
            y2 = 60 + (radius+60) * math.sin(math.radians(45))

            canvas.create_line(x1, y1, x2, y2, tags = "hangman")
        
        if(self.nMissChar >= 4):                                    # 오른팔
            x3 = 160 + radius * math.cos(math.radians(45))
            y3 = 60 + radius * math.sin(math.radians(45))
            x4 = 160 + (radius+60) * math.cos(math.radians(45))
            y4 = 60 + (radius+60) * math.sin(math.radians(45))

            canvas.create_line(x3, y3, x4, y4, tags = "hangman")

        if(self.nMissChar >= 5):                                    # 몸통
            x5 = 160
            y5 = 60 + radius
            x6 = 160
            y6 = 60 + radius + 60

            canvas.create_line(x5, y5, x6, y6, tags = "hangman")

        if(self.nMissChar >= 6):                                    # 왼쪽 다리
            x7 = 160
            y7 = 60 + radius + 60
            x8 = 160 - (radius+60) * math.cos(math.radians(45))
            y8 = 60 + (radius+60) * math.sin(math.radians(45)) + 60

            canvas.create_line(x7, y7, x8, y8, tags = "hangman")

        if(self.nMissChar >= 7):                                    # 오른 다리
            x9 = 160
            y9 = 60 + radius + 60
            x10 = 160 + (radius+60) * math.cos(math.radians(45))
            y10 = 60 + (radius+60) * math.sin(math.radians(45)) + 60

            canvas.create_line(x9, y9, x10, y10, tags = "hangman")
    
    def setWord(self):                                              # 새로운 단어를 선택하고 게임 (재)시작
        pass

    def guess(self, letter):                                        # 사용자가 입력한 글자를 반영
        self.draw()
        
# Initialize words, get the words from a file
infile = open("hangman.txt", "r")
words = infile.read().split()
word = None
    
window = Tk() # Create a window
window.title("행맨") # Set a title

def processKeyEvent(event):  
    global hangman, word

    if event.char >= 'a' and event.char <= 'z':                     # a ~ z까지 입력한 것을 word에 저장
        word = event.char
    elif event.keycode == 13:                                       # 엔터 입력 시, word에 저장된 값 전달
        hangman.guess(word)
    
width = 400
height = 280    
# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

random_number = randint(0, len(words) - 1)                          # 읽어온 단어들 전체 중 하나를 랜덤하게 선택

hangman = Hangman(words[random_number])                             # 랜덤하게 선택한 단어로 클래스 생성

# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()

window.mainloop() # Create an event loop
