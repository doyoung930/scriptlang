###
### 
###
from tkinter import*
import tkinter.ttk as ttk
import tkinter.font
# Button에 패러매터를 주기 위한 모듈
from functools import partial
import tkinter


### 기본 gui 생성함수
def program_gui():

    state_font = tkinter.font.Font(family = "나눔 고딕" , size = 10)
    state_text = ttk.Label(root, text = "[지역]", font = state_font)
    state_text.place( x= 315, y = 52)
    state_font = tkinter.font.Font(family = "나눔 고딕" , size = 10)
    state_text = ttk.Label(root, text = "[체육시설]", font = state_font)
    state_text.place( x= 20, y = 52)

    sports_values = ["축구장", "농구장", "수영장", "배드민턴", "탁구", "선택안함"]
    sportscombo = ttk.Combobox(root, values = sports_values)
    sportscombo.config(height=10,width = 25)
    sportscombo.config(state="readonly")
    sportscombo.set("체육시설을 고르시오.")
    sportscombo.place( x = 95, y = 50)

    # 지역 검색박스
    stateinput = ttk.Entry( root,font = state_font)
    stateinput.config(width = 22)
    stateinput.place(x = 370, y = 50)
    
    #검색 버튼
    SearchButton = Button(font = state_font, text="검색", command=onSearch)
    SearchButton.place(x= 540, y = 45)

    #리스트 박스
    s_listbox = Listbox(root)
    s_listbox.config(font = state_font, activestyle='none', selectmode = BROWSE)
    s_listbox.config(width = 38, height = 20)
    s_listbox.place(x = 20, y = 80)

# 검색 버튼 상호작용 함수
def onSearch():
    global SearchListBox

# 리스트 박스 함수
def sportsList():
    global s_list

#지도로 이동
def sports_map():
    #지도로 이동하는 버튼
    #map_image = PhotoImage(file = "C:/develop/map.gif")
    map_button = Button( root, text = "지도로 이동", height = 5, width = 10)
    map_button.place( x = 500, y= 300) 

#이메일 보내기
def Send_email():
    mail_button = Button( root, text = "메일로 전송", height = 5, width = 10)
    mail_button.place( x = 400, y= 300)

##############
def main():
##############s
    #선언
    global root
    root = Tk()
    #사이즈
    root.geometry ("600x400+450+100")
    #타이틀
    root.title("스언어 팀플")
    #창크기 변환 X
    root.resizable(False, False )

    # 폰트
    global font
    font = tkinter.font.Font(family = "나눔 고딕" , size = 20)
   
    win_text= tkinter.Label(root, text = "[체육시설검색프로그램]", font = font)
    win_text.pack()
    
    program_gui()
    sports_map()
    Send_email()


    root.mainloop()

    

 

main()