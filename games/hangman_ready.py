import math
from tkinter import * # Import tkinter
from random import randint
    
class Hangman:
    hiddenWord, guessWord, nMissedLetters = [], [], []    # 파일에서 찾은 단어, 맞추고 있는 단어, 틀린 단어 리스트
    nCorrectChar, nMissChar = 0, 0                          # 맞춘 개수, 틀린 개수
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
        
        if(self.nMissChar >= 1):
            radius = 20 # 반지름
            canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger

        if(self.nMissChar >= 2):
        # Draw the circle
            canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger

        if(self.nMissChar >= 3):
        # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
            x1 = 160 - radius * math.cos(math.radians(45))
            y1 = 60 + radius * math.sin(math.radians(45))
            x2 = 160 - (radius+60) * math.cos(math.radians(45))
            y2 = 60 + (radius+60) * math.sin(math.radians(45))

            canvas.create_line(x1, y1, x2, y2, tags = "hangman")
    
    def setWord(self):
        pass

    def guess(self, letter):
        self.draw()
        
# Initialize words, get the words from a file
infile = open("hangman.txt", "r")
words = infile.read().split()
word = None
    
window = Tk() # Create a window
window.title("행맨") # Set a title

def processKeyEvent(event):  
    global hangman, word

    if event.char >= 'a' and event.char <= 'z':
        word = event.char
    elif event.keycode == 13:
        hangman.guess(word)
    
width = 400
height = 280    
# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

random_number = randint(0, len(words) - 1)

hangman = Hangman(words[random_number])

# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()

window.mainloop() # Create an event loop
