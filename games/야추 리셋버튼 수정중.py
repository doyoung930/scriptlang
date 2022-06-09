### Yahtzee_이도_이도영.py

from tkinter import *
from tkinter import font
import tkinter.messagebox
import random

class Configuration:
    configs = ["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
               "Upper Scores", "Upper Bonus(35)", "Three of a kind", "Four of a kind", "Full House(25)",
               "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance", "Lower Scores", "Total"]

    def getConfigs(): 
        return Configuration.configs

    def score(row, d):
        if (row >= 0 and row <6):
            return Configuration.scoreUpper(d, row + 1)
        elif (row == 8):
            return Configuration.scoreThreeOfAKind(d)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(d)
        elif (row == 10):
            return Configuration.scoreFullHouse(d)
        elif (row == 11):
            return Configuration.scoreSmallStraight(d)
        elif (row == 12):
            return Configuration.scoreLargeStraight(d)
        elif (row == 13):
            return Configuration.scoreYahtzee(d)
        elif (row == 14):
            return Configuration.sumDie(d)

    # Upper Section 구성 (Ones, Twos, Threes, ...)에 대해 주사위 점수를 매김
    # 예)num이 1이면 "Ones"구성의 주사위 점수를 반환함
    def scoreUpper(d, num): 
        result=0
        for i in d:
           if i.getRoll()==num:
               result+=num
        return result


    def scoreThreeOfAKind(d):
        dic={}
        result=0
        for i in d:
            result += i.getRoll()
            try:
                dic[i.getRoll()] += 1
            except:
                dic[i.getRoll()] = 1

        for key,val in dic.items():
            if val>=3:
                return result
        return 0


    def scoreFourOfAKind(d):
        dic = {}
        result = 0
        for i in d:
            result += i.getRoll()
            try:
                dic[i.getRoll()] += 1
            except:
                dic[i.getRoll()] = 1

        for key, val in dic.items():

            if val >= 4:
                return result
        return 0

    def scoreFullHouse(d):
        dic = {}
        L=[]
        result = 0
        for i in d:
            result += i.getRoll()
            try:
                dic[i.getRoll()] += 1
            except:
                dic[i.getRoll()] = 1

        for key, val in dic.items():
            L.append(val)

        if 3 in L and 2 in L:
            return 25
        return 0
    # 1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
    # 1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5
    def scoreSmallStraight(d):
        dl = [0] * 6
        for i in range(5):
            dl[d[i].getRoll() - 1] = 1

        result = False
        for i in range(3):
            cnt = 0
            for j in range(i, i + 4):
                if (dl[j] == 1):
                    cnt += 1
            if cnt >= 4:
                result = True
                break
        if result:
            return 30
        else:
            return 0

    # 1 2 3 4 5 혹은 2 3 4 5 6 검사
    def scoreLargeStraight(d):
        result=[]

        for x in d:
            result.append(x.getRoll())
        a=set(result)
        if a =={1 ,2, 3, 4, 5}:
            return 40
        elif a == {2 , 3 , 4 , 5, 6}:
            return 40
        else:
            return 0

    def scoreYahtzee(d):
        dic = {}
        result = 0
        for i in d:
            result += i.getRoll()
            try:
                dic[i.getRoll()] += 1
            except:
                dic[i.getRoll()] = 1

        for key, val in dic.items():

            if val == 5:
                return 50
        return 0

    def sumDie(d):
        result=0
        for i in d:
            result+=i.getRoll()
        return result

class Dice:
    def rollDie(self):
        self.roll=random.randint(1,6)
    def getRoll(self):
        return self.roll

class Player:
    UPPER = 6 # upper category 6개
    LOWER = 7 # lower category 7개
    def __init__(self,name):
        self.name = name
        self.scores=[0 for i in range(self.UPPER+self.LOWER)] #13개category점수
        #13개 category 사용여부
        self.used=[False for i in range(self.UPPER+self.LOWER)]
    def setScore(self, score, index):
        self.scores[index]=score
    def setAtUsed(self, index):
        self.used[index] = True
    def defaultUsed(self, index):
        self.used[index] = False
    def getUpperScore(self):
        result=0
        for i in range(self.UPPER):
                result+=self.scores[i]
        return result

    def getLowerScore(self):
        result=0
        for i in range(self.UPPER,self.UPPER + self.LOWER):
            result+=self.scores[i]
        return result
    def getUsed(self):
        return self.used
    def getTotalScore(self):
        return sum(self.scores)
    def toString(self):
        return self.name
    def allLowerUsed(self): #lower category 7개 모두 사용되었는가 ?
        for i in range(self.UPPER,self.UPPER + self.LOWER):
            if (self.used[i] == False):
                return False
        return True
    def allUpperUsed(self): #upper category 6개 모두 사용되었는가 ?
        for i in range(self.UPPER):
            if (self.used[i] == False):
                return False
        return True
                            #UpperScores, UpperBonus 계산에 활용


class YahtzeeBoard:
    UPPERTOTAL = 6  # UpperScore
    UPPERBONUS = 7  # UpperBonus
    LOWERTOTAL = 15  # LowerScore
    TOTAL = 16  # Total
    dice = []  # Dice 객체 리스트
    diceButtons = []  # diceButton 리스트
    fields = []  # 각 플레이어 점수판 2차원 리스트
    # 열 플레이어, 0열=플레이어1, 1열=플레이어2,…
    # 17행 점수 = 카테고리13행 + upperScore + upperBonus + LowerScore + Total
    Restart_Button = None                   # 다시 시작 버튼
    players = []  # player 객체 리스트
    numPlayers = 0
    player = 0  # 플레이어 순서를 제어
    round = 0  # 13라운드를 제어
    roll = 0  # 각 라운드 마다 3번 굴리기 roll를 할 수 있음

    def __init__(self):
        self.InitPlayers()

    def InitPlayers(self):  # player window 생성하고 최대 10명까지 플레이어 설정
        self.pwindow = Tk()

        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        self.label = []
        self.entry = []
        self.label.append(Label(self.pwindow, text="플레이어 명수", font=self.TempFont))
        self.label[0].grid(row=0, column=0)
        for i in range(1, 11):
            self.label.append(Label(self.pwindow, text="플레이어" + str(i) + " 이름",
                                font=self.TempFont))
            self.label[i].grid(row=i, column=0)
        for i in range(11):
            self.entry.append(Entry(self.pwindow, font=self.TempFont))
            self.entry[i].grid(row=i, column=1)
        Button(self.pwindow, text="Yahtzee 플레이어 설정 완료",
           font=self.TempFont, command=self.playerNames).grid(row=11, column=0)
        self.pwindow.mainloop()

    def playerNames(self):  # 플레이어 설정 완료 버튼 누르면 실행되는 함수
        self.numPlayers = int(self.entry[0].get())

        for i in range(1, self.numPlayers + 1):
            self.players.append(Player(str(self.entry[i].get())))
        self.pwindow.destroy()
        self.initInterface()  # Yahtzee 보드판 플레이어 명수 만큼 생성

    def initInterface(self):  # Yahtzee 보드 윈도우 생성
        self.window = Tk("YahtzeeGame")
        self.window.geometry("1600x800")
        self.TempFont = font.Font(size=16, weight='bold', family ='Consolas')
        for i in range(5):  # Dice 객체 5개 생성
            self.dice.append(Dice())
        self.rollDice = Button(self.window, text='RollDice', font = self.TempFont,
                      command = self.rollDiceListener)# Roll
        self.rollDice.grid(row=0, column=0)
        for i in range(5):  # dice 버튼 5개 생성
            self.diceButtons.append(Button(self.window, text='?',font = self.TempFont, width=8, command = lambda row=i: self.diceListener(row)))
            # 각각의 dice 버튼에 대한 이벤트 처리 diceListener 연결
            # 람다 함수를 이용하여 diceListener 매개변수 설정하면 하나의 Listener로 해결
            self.diceButtons[i].grid(row=i + 1, column=0)
        
        self.Restart_Button = Button(self.window, text='다시 시작', font=self.TempFont, width=8, command=self.Reset)
        self.Restart_Button.grid(row=self.TOTAL + 1, column=0)


        for i in range(self.TOTAL + 2):  # i행 : 점수
            Label(self.window, text=Configuration.configs[i], font=self.TempFont).grid(row=i, column=1)
            for j in range(self.numPlayers):  # j열 : 플레이어
                if (i == 0):  # 플레이어 이름 표시
                    Label(self.window, text=self.players[j].toString(), font=self.TempFont).grid(
                        row=i, column=2 + j)
                else:
                    if (j == 0):  # 각 행마다 한번씩 리스트 추가, 다중 플레이어 지원
                        self.fields.append(list())
    # i-1행에 플레이어 개수 만큼 버튼 추가하고 이벤트 Listener 설정, 매개변수 설정
                    self.fields[i - 1].append(Button(self.window, text="", font=self.TempFont, width=8,
                                    command=lambda row=i - 1: self.categoryListener(row)))
                    self.fields[i - 1][j].grid(row=i, column=2 + j)
    # 누를 필요없는 버튼은 disable 시킴
                    if (j != self.player or (i - 1) == self.UPPERTOTAL or (i - 1) == self.UPPERBONUS
                        or (i - 1) == self.LOWERTOTAL or (i - 1) == self.TOTAL):
                        self.fields[i - 1][j]['state'] = 'disabled'
                        self.fields[i - 1][j]['bg'] = 'light gray'
    # 상태 메시지 출력
        self.bottomLabel = Label(self.window, text=self.players[self.player].toString() +
                                               "차례: Roll Dice 버튼을 누르세요", width=35, font=self.TempFont)
        self.bottomLabel.grid(row=self.TOTAL + 2, column=0)
        self.window.mainloop()
    
    def Reset(self):
        self.player = 0  
        self.round = 0  
        self.roll = 0

        for i in range(self.TOTAL + 1):
            for j in range(self.numPlayers):
                self.players[j].defaultUsed(i)
                self.players[j].setScore(0, i)
                self.fields[i][j].configure(text=str(''))

    def rollDiceListener(self):  # rollDiceListener
        for i in range(5):
            if (self.diceButtons[i]['state'] != 'disabled'):
                self.dice[i].rollDie()
                self.diceButtons[i].configure(text=str(self.dice[i].getRoll()))
            else:
                pass
        if (self.roll == 0 or self.roll == 1):
            self.roll += 1
            self.rollDice.configure(text="Roll Again")
            self.bottomLabel.configure(text="보관할 주사위 선택 후 Roll Again")
        elif (self.roll == 2):
            self.bottomLabel.configure(text="카테고리를 선택하세요")
            self.rollDice['state'] = 'disabled'
            self.rollDice['bg'] = 'light gray'

    def diceListener(self, row):  # DiceListener
        if self.roll!=0 :
            if self.diceButtons[row]['state']!='disabled':
                self.diceButtons[row]['state'] = 'disabled'
                self.diceButtons[row]['bg'] = 'light gray'

    def categoryListener(self, row):  # categoryListener
        if(self.roll != 0):                         # 주사위를 한 번이라도 돌렸는가?
            score = Configuration.score(row, self.dice)  # 점수 계산

            index = row
            if (row > 7):
                index = row - 2
        # 선택한 카테고리 점수 적고 disable 시킴
            self.players[self.player].setScore(score, index)
            self.players[self.player].setAtUsed(index)
            self.fields[row][self.player].configure(text=str(score))
            self.fields[row][self.player]['state'] = 'disabled'
            self.fields[row][self.player]['bg'] = 'light gray'
            # UPPER category가 전부 사용되었으면 UpperScore, UpperBonus 계산
            if (self.players[self.player].allUpperUsed()):
                self.fields[self.UPPERTOTAL][self.player].configure(text=
                                                                str(self.players[self.player].getUpperScore()))
                if (self.players[self.player].getUpperScore() > 63):
                    self.fields[self.UPPERBONUS][self.player].configure(text="35")  # UPPERBONUS=7
                else:
                    self.fields[self.UPPERBONUS][self.player].configure(text="0")  # UPPERBONUS=7

            if (self.players[self.player].allLowerUsed()):
                self.fields[self.LOWERTOTAL][self.player].configure(text=str(self.players[self.player].getLowerScore()))
            # UPPER category와 LOWER category가 전부 사용되었으면 TOTAL 계산
            if (self.players[self.player].allUpperUsed() and self.players[self.player].allLowerUsed()):
                self.fields[self.TOTAL][self.player].configure(text=str(self.players[self.player].getTotalScore()))
            # 다음 플레이어로 넘어가고 선택할 수 없는 카테고리들은 disable 시킴
            self.player = (self.player + 1) % self.numPlayers

            for i in range(self.TOTAL + 1):
                for j in range(self.numPlayers):
                    self.fields[i][j]['state'] = 'disabled'
                    self.fields[i][j]['bg'] = 'light gray'

                    if (j != self.player or (i) == self.UPPERTOTAL or (i) == self.UPPERBONUS
                            or (i) == self.LOWERTOTAL or (i)  == self.TOTAL):
                            self.fields[i][j]['state'] = 'disabled'
                            self.fields[i][j]['bg'] = 'light gray'
                    elif  self.fields[i][self.player]['text']:
                        self.fields[i][self.player]['state'] = 'disabled'
                        self.fields[i][self.player]['bg'] = 'light gray'
                    else:
                        self.fields[i][self.player]['state'] = 'normal'
                        self.fields[i][self.player]['bg'] = 'SystemButtonFace'
            if(self.player==0):
                self.round+=1
            if(self.round==13):
                d={}
                for x in self.players:
                    d[x.toString()]=x.getTotalScore()
                val=max(d.values())
                resurtList=list(key for key,value in d.items() if value ==val)
                if len(resurtList)==1:
                    a="승자는: "+resurtList[0]+" 입니다."
                    self.winnertag=Label(self.window, text=a, font=self.TempFont).grid(row=10,column=0)
                else:
                    resultstr=""
                    for x in resurtList:
                        resultstr+=resultstr+x+","
                    resultstr+="가 비겼습니다."
                    self.winnertag = Label(self.window, text=resultstr, font=self.TempFont).grid(row=10,column=0)

            #비김 , 승자 처리
            pass

        self.roll=0
        self.dice=[]
        for i in range(5):  # Dice 객체 5개 생성
            self.dice.append(Dice())
        self.rollDice .configure(text='RollDice')
        self.rollDice['state'] = 'normal'
        self.rollDice['bg'] = 'SystemButtonFace'
        for i in range(5):  # dice 버튼 5개 생성
            self.diceButtons[i].configure(text="?")
            self.diceButtons[i]['state'] = 'normal'
            self.diceButtons[i]['bg'] = 'SystemButtonFace'
        self.bottomLabel.configure(text=self.players[self.player].toString() +
                                   "차례: Roll Dice 버튼을 누르세요")
        print(self.round)
YahtzeeBoard()
