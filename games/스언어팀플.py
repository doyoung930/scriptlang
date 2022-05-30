###
### 
###
# xml
from doctest import script_from_examples
from xml.etree.ElementTree import *
from xml.dom.minidom import *
import http.client
import urllib.request
from xml.dom.minidom import parseString
from functools import partial

#tk
from tkinter import*
import tkinter.ttk as ttk
import tkinter.font


# Button에 패러매터를 주기 위한 모듈
from functools import partial
import tkinter


###
###
###

### XML
def LoadXMLFromFile():
    #fileName = 
    pass

### 기본 gui 생성함수
def program_gui():

    state_font = tkinter.font.Font(family = "나눔 고딕" , size = 10)
    state_text = ttk.Label(root, text = "[지역]", font = state_font)
    state_text.place( x= 315, y = 52)
    state_font = tkinter.font.Font(family = "나눔 고딕" , size = 10)
    state_text = ttk.Label(root, text = "[체육시설]", font = state_font)
    state_text.place( x= 20, y = 52)

    global sportscombo
    sports_values = ["축구장", "농구장", "수영장", "실내스포츠(배드민턴, 탁구)"]
    sportscombo = ttk.Combobox(root, values = sports_values)
    sportscombo.config(height=10,width = 25)
    sportscombo.config(state="readonly")
    sportscombo.set("체육시설을 고르시오.")
    sportscombo.place( x = 95, y = 50)

    # 지역 검색박스
    global stateinput
    stateinput = ttk.Entry( root,font = state_font)
    stateinput.config(width = 22)
    stateinput.place(x = 370, y = 50)
    
    #검색 버튼
    global SearchButton
    SearchButton = Button(font = state_font, text="검색", command=partial(onSearch, sportscombo))
    SearchButton.place(x= 540, y = 45)

    # 스포츠 센터 리스트 박스
    global s_listbox
    s_listbox = Listbox(root,borderwidth=12, relief='ridge')
    s_listbox.config(font = state_font, activestyle='none', selectmode = BROWSE)
    s_listbox.config(width = 38, height = 20)
    s_listbox.place(x = 20, y = 80)
    s_listbox.bind('<<ListboxSelect>>', event_for_listbox)    ## 고르면 리스트박스 이벤트 함수로
    
    # 스포츠 센터 정보를 주는 리스트박스
    global info_listbox
    info_listbox = Listbox(root,borderwidth=12, relief='ridge')
    info_listbox.config(font = state_font, activestyle='none', selectmode = BROWSE)
    info_listbox.config(width = 35, height = 20)
    info_listbox.place(x = 320 , y = 80)

    # global info_Text
    # info_Text = Text(root,borderwidth=12, relief='ridge')
    # info_Text.config(wrap = 'c', font = state_font)
    # info_Text.config(width = 35, height = 21)
    # info_Text.place(x = 320, y = 80)
   
    # 메일 버튼
    mail_button = Button( root, text = "메일로 전송", height = 5, width = 10, command=partial(Send_email))
    mail_button.place( x = 400, y= 400)

    # 지도 버튼
    map_button = Button( root, text = "지도로 이동", height = 5, width = 10, command=partial(sports_map))
    map_button.place( x = 500, y= 400) 


# #리스트 박스 이벤트
def event_for_listbox(event):
    global info_listbox
    global elements
    global parseData
    global strXml
    info_listbox.delete(0,info_listbox.size())
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)
    
    info_listbox.insert(1, data)
    

# 검색 버튼 상호작용 함수
def onSearch(sports):
    global s_listbox
    s_listbox.delete(0, s_listbox.size())
    
    sels = s_listbox.curselection()
        
    iSearchIndex=\
    0 if len(sels) == 0 else s_listbox.curselection()[0]
        
    if iSearchIndex == 0:
        Searchsport(sports.get())
    elif iSearchIndex == 1:
        pass
    elif iSearchIndex == 2:
        pass
    elif iSearchIndex == 3:
        pass
# 검색 -> 스포츠
def Searchsport(sport):
    from xml.etree import ElementTree

    global sportscombo
  #  sportscombo.delete(0, sportscombo.size())

    server = "openapi.gg.go.kr"

    #key_value = 3cccb5986c79462dae3acd235fa8a54f

    conn = http.client.HTTPSConnection(server)

    if(sport == "농구장"):
        conn.request(
            "GET",
            "/PublicLivelihood?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )

    #conn = http.client.HTTPSConnection(server)
    elif(sport == "축구장"):
        conn.request(
            "GET",
            "/PublicTrainingFacilitySoccer?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )

    #conn = http.client.HTTPSConnection(server)\
    elif(sport == "수영장"):
        conn.request(
            "GET",
            "/PublicSwimmingPool?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )

    #conn = http.client.HTTPSConnection(server)
    elif(sport == "실내스포츠(배드민턴, 탁구)"):
        conn.request(
            "GET",
            "/PublicGameOfBallGymnasium?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )

    res = conn.getresponse()

    global strXml
    global stateinput
    global parseData
    global elements

    if int(res.status) == 200:
        print("읽어 오는데 성공")
        strXml = res.read().decode('utf-8')
       # print(parseString(res.read().decode('utf-8')).toprettyxml())
    else:
        print('HTTP request failed : ', res.reason)
    parseData = ElementTree.fromstring(strXml)
    elements = parseData.iter('row')
    i = 1
    for item in elements: # " row“ element들
        part_el = item.find('SIGUN_NM')
        if stateinput.get() not in part_el.text:
            continue
        _text = '[' + str(i) + '] ' + \
            getStr(item.find('FACLT_NM').text) + \
            ' , ' + getStr(item.find('SIGUN_NM').text) + \
            ' , ' + getStr(item.find('REFINE_ROADNM_ADDR').text)
            
            
        s_listbox.insert(i-1,_text)
        i = i+1

def getStr(s):
    return '' if not s else s

### UIR 생성 함수
# def userURIBuilder(uri, **user):
#     str = uri +"?"
#     for key in user.keys():
#         str += key + "=" + user[key] + "&"
#     return str



#지도로 이동
def sports_map():
    global location
    location = tkinter.Toplevel()
    location.geometry ("500x600+550+100")
    location.title("지도")
    location.resizable(False, False )
    location_font = tkinter.font.Font(family = "나눔 고딕" , size = 15)
    
    location_text= tkinter.Label(location, text = "[지도]", font = location_font)
    location_text.pack()

#이메일 보내기
def Send_email():
    global mail
    mail = tkinter.Toplevel()
    mail.geometry ("350x100+650+400")
    mail.title("메일")
    mail.resizable(False, False )
    mail_font = tkinter.font.Font(family = "나눔 고딕" , size = 15)
    s_mail_font = tkinter.font.Font(family = "나눔 고딕" , size = 10)
    
    mail_text= tkinter.Label(mail, text = "[메일 전송]", font = mail_font)
    mail_text.pack()
        # 지역 검색박스
    mailinput = ttk.Entry( mail,font = s_mail_font)
    mailinput.config(width = 22)
    mailinput.pack()
    
    #검색 버튼
    global SearchButton
    SearchButton = Button(mail, font = s_mail_font, text="전송")
    SearchButton.pack()
##############
def main():
##############s
    #선언
    global root
    root = Tk()
    #사이즈
    root.geometry ("600x700+450+100")
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




    root.mainloop()

    

 

main()