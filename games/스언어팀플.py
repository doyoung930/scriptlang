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
   
# #리스트 박스 이벤트
def event_for_listbox(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)

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
<<<<<<< HEAD
    elif(sport == "실내스포츠(배드민턴, 탁구)"):
=======
    elif(sport == "배드민턴" or sport == "탁구"):
>>>>>>> 52e1e01e5cee6c026d3db8218bf49769a3a3a94c
        conn.request(
            "GET",
            "/PublicGameOfBallGymnasium?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )

    res = conn.getresponse()

    global strXml
    global stateinput

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
            ' , ' + getStr(item.find('REFINE_LOTNO_ADDR').text)
            # ' , ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + \
            # ' , ' + getStr(item.find('REFINE_WGS84_LAT').text)    
            # ' , ' + getStr(item.find('GYM_STND').text) + \
            # ' , ' + getStr(item.find('BUILD_AR').text) + \
            # ' , ' + getStr(item.find('SWIMPL_AR').text) + \
            # ' , ' + getStr(item.find('SWIMPL_STND').text) + \
            # ' , ' + getStr(item.find('TRAINRM_RM_MATR').text) + \
            # ' , ' + getStr(item.find('EGYM_POSBL_ETRS_CONT').text) + \
            # ' , ' + getStr(item.find('ACEPTNC_PSNCNT').text) + \

            
            
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
    #지도로 이동하는 버튼
    #map_image = PhotoImage(file = "C:/develop/map.gif")
    map_button = Button( root, text = "지도로 이동", height = 5, width = 10)
    map_button.place( x = 500, y= 400) 

#이메일 보내기
def Send_email():
    mail_button = Button( root, text = "메일로 전송", height = 5, width = 10)
    mail_button.place( x = 400, y= 400)

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
    sports_map()
    Send_email()


    root.mainloop()

    

 

main()