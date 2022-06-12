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
from PIL import ImageTk


# Button에 패러매터를 주기 위한 모듈
from functools import partial
import tkinter

#지도
import tkintermapview

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
    sports_values = ["축구장", "농구장", "수영장", "실내스포츠(배드민턴, 탁구)", "선택안함"]
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
    s_frame = Frame(root)
    s_frame.place(x = 20, y = 80)
    s_scrollbar = Scrollbar(s_frame)
    s_scrollbar.pack(side = "right", fill = "y")

    s_listbox = Listbox(s_frame, borderwidth=12, relief='ridge', yscrollcommand = s_scrollbar.set)
    s_listbox.config(font = state_font, activestyle='none', selectmode = BROWSE)
    s_listbox.config(width = 36, height = 20)
    s_listbox.pack(side = "left")
 
    s_listbox.bind('<<ListboxSelect>>', event_for_listbox)    ## 고르면 리스트박스 이벤트 함수로

    s_scrollbar.config(command= s_listbox.yview )


#####
    # s_scrollbar = Scrollbar(root)
    # s_listbox = Listbox(root,borderwidth=12, relief='ridge', yscrollcommand = s_scrollbar.set)
    # s_listbox.config(font = state_font, activestyle='none', selectmode = BROWSE)
    # s_listbox.config(width = 36, height = 20)
    # s_listbox.place(x = 20, y = 80)
    # s_listbox.bind('<<ListboxSelect>>', event_for_listbox)    ## 고르면 리스트박스 이벤트 함수로
    # s_scrollbar.config(command= s_listbox.yview )
    # s_scrollbar.place( x= 297, y= 80)


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
    
    #mail_image = PhotoImage(file = "C:/Users/doyou/OneDrive/문서/GitHub/scriptlang/games/mailicon2.png")
    mail_button = Button( root, text = "메일로 전송", height = 5, width = 10, command=partial(Send_email))
    #mail_button = Button( root, image = mail_image, command=partial(Send_email))
    mail_button.place( x = 500, y= 500)

    # 지도 버튼
    map_button = Button( root, text = "지도로 이동", height = 5, width = 10, command=partial(sports_map))
    map_button.place( x = 500, y= 400) 


# #리스트 박스 이벤트
def event_for_listbox(event):
    global info_listbox
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

    server = "openapi.gg.go.kr"

    basket_conn = http.client.HTTPSConnection(server)
    basket_conn.request(
            "GET",
            "/PublicLivelihood?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )

    foot_conn = http.client.HTTPSConnection(server)
    foot_conn.request(
            "GET",
            "/PublicTrainingFacilitySoccer?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )
    
    swim_conn = http.client.HTTPSConnection(server)
    swim_conn.request(
            "GET",
            "/PublicSwimmingPool?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )
    
    inside_conn = http.client.HTTPSConnection(server)
    inside_conn.request(
            "GET",
            "/PublicGameOfBallGymnasium?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )
        

    global stateinput
    global s_listbox

    i = 1

    # 농구 데이터-------------------------------------------------------------
    if(sport == "농구장" or sport == "선택안함"):
        bs_num = 0
        basket_res = basket_conn.getresponse()

        if int(basket_res.status) == 200:
            #print("농구장 읽어 오는데 성공")
            basket_strXml = basket_res.read().decode('utf-8')
        else:
            print('HTTP request failed : ', basket_res.reason)

        basket_parseData = ElementTree.fromstring(basket_strXml)
        basket_elements = basket_parseData.iter('row')

        for item in basket_elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            if stateinput.get() not in part_el.text:
                continue
            _text = '[' + str(i) + '] ' + \
                getStr(item.find('FACLT_NM').text) + \
                ' , ' + getStr(item.find('SIGUN_NM').text)
            
            bs_num += 1
            s_listbox.insert(i-1,_text)
            i = i+1
    
    # 축구 데이터-------------------------------------------------------------
    if(sport == "축구장" or sport == "선택안함"):
        ft_num = 0
        foot_res = foot_conn.getresponse()

        if int(foot_res.status) == 200:
            #print("축구장 읽어 오는데 성공")
            foot_strXml = foot_res.read().decode('utf-8')
        else:
            print('HTTP request failed : ', foot_res.reason)
            
        foot_parseData = ElementTree.fromstring(foot_strXml)
        foot_elements = foot_parseData.iter('row')

        for item in foot_elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            if stateinput.get() not in part_el.text:
                continue
            _text = '[' + str(i) + '] ' + \
                getStr(item.find('FACLT_NM').text) + \
                ' , ' + getStr(item.find('SIGUN_NM').text)
                
            ft_num += 1

            s_listbox.insert(i-1,_text)
            i = i+1
    
    # 수영 데이터-------------------------------------------------------------
    if(sport == "수영장" or sport == "선택안함"):
        sw_num = 0
        swim_res = swim_conn.getresponse()

        if int(swim_res.status) == 200:
            #print("수영장 읽어 오는데 성공")
            swim_strXml = swim_res.read().decode('utf-8')
        else:
            print('HTTP request failed : ', swim_res.reason)
            
        swim_parseData = ElementTree.fromstring(swim_strXml)
    
        swim_elements = swim_parseData.iter('row')

        for item in swim_elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            if stateinput.get() not in part_el.text:
                continue
            _text = '[' + str(i) + '] ' + \
                getStr(item.find('FACLT_NM').text) + \
                ' , ' + getStr(item.find('SIGUN_NM').text)
                
            sw_num += 1

            s_listbox.insert(i-1,_text)
            i = i+1
    
    # 실내스포츠 데이터-------------------------------------------------------------
    if(sport == "실내스포츠(배드민턴, 탁구)" or sport == "선택안함"):
        ins_num = 0
        inside_res = inside_conn.getresponse()

        if int(inside_res.status) == 200:
            #print("실내스포츠 읽어 오는데 성공")
            inside_strXml = inside_res.read().decode('utf-8')
        else:
            print('HTTP request failed : ', inside_res.reason)
            
        inside_parseData = ElementTree.fromstring(inside_strXml)
        inside_elements = inside_parseData.iter('row')

        for item in inside_elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            if stateinput.get() not in part_el.text:
                continue
            _text = '[' + str(i) + '] ' + \
                getStr(item.find('FACLT_NM').text) + \
                ' , ' + getStr(item.find('SIGUN_NM').text)
                
            ins_num += 1

            s_listbox.insert(i-1,_text)
            i = i+1

    # 스크롤 바
    global scrollbar
    
    scrollbar = Scrollbar(s_listbox)
    #scrollbar.place(x = 300 , y = 80)
    scrollbar.set
    scrollbar.config(command=s_listbox.yview)

    # 그래프 그리기
    drawGraph(sport, [{'name' : '농구', "value" : bs_num}, {'name' :'축구', "value" : ft_num},\
        {'name' :'수영', "value" : sw_num}, {'name' :'실내', "value" : ins_num}])

# 그래프 그리는 함수
def drawGraph(sport, data):
    # 그래프 크기는, [left, top, right, bottom] = [20, 400, 480, 650], 가로 = 460px, 세로 = 250px
    global root
    if(sport == "선택안함"):
        nData = len(data)
        nMax = max(data, key=lambda x:x['value'])
        nMin = min(data, key=lambda x:x['value'])

        canvasWidth = 460
        canvasHeight = 250

        canvas = Canvas(root, width=canvasWidth, height=canvasHeight, bg='white')
        canvas.place(x=20, y=400)

        canvas.create_rectangle(20, 400, 460, 250, fill='white', tag="graph")

        if nMax["value"] == 0:                           # 만약 데이터를 못 불러왔다면 끝낸다
            return
        
        rectHeight = (canvasHeight // nData)
        right = (canvasWidth - 40)
        maxWidth = canvasWidth - 80

        for i in range(nData):
            if nMax["value"] == data[i]["value"]: 
                color="red"
            elif nMin["value"] == data[i]["value"]:
                color = "blue"
            else:
                color = "gray"

            curWidth = maxWidth * data[i]["value"] / nMax["value"]
            left = right - curWidth
            top = i * rectHeight
            bottom = (i + 1) * rectHeight

            canvas.create_rectangle(left, top, right, bottom, fill=color, tag="graph")

            canvas.create_text(left - 20, (top + bottom) // 2, text=data[i]["value"])
            canvas.create_text(right + 20, (top + bottom) // 2, text=data[i]["name"])


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
    map_widget = tkintermapview.TkinterMapView(location, width=800, height=500, corner_radius=0)
    map_widget.pack()
    map_widget.set_position(37.012603584211, 127.32631686988)
    map_widget.set_address("경기 안성시 보개면 종합운동장로 162", marker=True)
    map_widget.set_zoom(15)
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