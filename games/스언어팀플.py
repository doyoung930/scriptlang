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

#mail
#gmail_htmlsend.py
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

##gmail_send.py
from email.mime.text import MIMEText

# Button에 패러매터를 주기 위한 모듈
from functools import partial
import tkinter

#지도
import tkintermapview

#메세지 박스
from tkinter import messagebox
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

    # # 스포츠 리스트 프레임
    # global s_frame
    # s_frame = Frame(root, borderwidth=12)
    # s_frame.config(width=38, height=20)
    # s_frame.place(x=20, y=80)

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

    # 캔버스 그리기
    drawCanvas()
   
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
    global _text1
    global _text7
    global logt
    global lat
    global building

    global info_listbox
    info_listbox.delete(0,info_listbox.size())
    selection = event.widget.curselection()

    global sport_num

    find_in_dontselect = False                      # 선택 안 함에서 찾았는가?

    if selection:
        index = selection[0]
        data = event.widget.get(index).split(':')

        if(sport_num != "선택안함"):
            if(sport_num == "농구"):
                elements = get_xml_basket()
            elif(sport_num == "축구"):
                elements = get_xml_soccer()
            elif(sport_num == "수영"):
                elements = get_xml_swim()
            elif(sport_num == "실내"):
                elements = get_xml_inside()

            for item in elements:
                name = item.find('FACLT_NM').text
                if name == data[1]:
                    _text1 = "시설명 : " + getStr(item.find('FACLT_NM').text)
                    _text2 ='시군명 : ' + getStr(item.find('SIGUN_NM').text)
                    _text3 ="도로명 주소 : " + getStr(item.find('REFINE_ROADNM_ADDR').text)
                    _text4 = "연락처 : " + getStr(item.find('CONTCT_NO').text)
                    _text5 = "홈페이지 주소 : " + getStr(item.find('HMPG_ADDR').text)
                    _text6 = "면적(건축) : " + getStr(item.find('BUILD_AR').text) + "m^2"
                    _text7 = getStr(item.find('REFINE_LOTNO_ADDR').text)
                    logt = getStr(item.find('REFINE_WGS84_LOGT').text)
                    lat = getStr(item.find('REFINE_WGS84_LAT').text)
                    building = getStr(item.find('FACLT_NM').text)
                    break
        
        # 선택 안 했다면 모든 xml에서 다 찾아
        else:
            elements = get_xml_basket()
            for item in elements:
                name = item.find('FACLT_NM').text
                if name == data[1]:
                    find_in_dontselect = True
                    _text1 = "시설명 : " + getStr(item.find('FACLT_NM').text)
                    _text2 ='시군명 : ' + getStr(item.find('SIGUN_NM').text)
                    _text3 ="도로명 주소 : " + getStr(item.find('REFINE_ROADNM_ADDR').text)
                    _text4 = "연락처 : " + getStr(item.find('CONTCT_NO').text)
                    _text5 = "홈페이지 주소 : " + getStr(item.find('HMPG_ADDR').text)
                    _text6 = "면적(건축) : " + getStr(item.find('BUILD_AR').text) + "m^2"
                    _text7 = getStr(item.find('REFINE_LOTNO_ADDR').text)
                    logt = getStr(item.find('REFINE_WGS84_LOGT').text)
                    lat = getStr(item.find('REFINE_WGS84_LAT').text)
                    building = getStr(item.find('FACLT_NM').text)
                    break
            if(not find_in_dontselect):
                elements = get_xml_soccer()
                for item in elements:
                    name = item.find('FACLT_NM').text
                    if name == data[1]:
                        find_in_dontselect = True
                        _text1 = "시설명 : " + getStr(item.find('FACLT_NM').text)
                        _text2 ='시군명 : ' + getStr(item.find('SIGUN_NM').text)
                        _text3 ="도로명 주소 : " + getStr(item.find('REFINE_ROADNM_ADDR').text)
                        _text4 = "연락처 : " + getStr(item.find('CONTCT_NO').text)
                        _text5 = "홈페이지 주소 : " + getStr(item.find('HMPG_ADDR').text)
                        _text6 = "면적(건축) : " + getStr(item.find('BUILD_AR').text) + "m^2"
                        _text7 = getStr(item.find('REFINE_LOTNO_ADDR').text)
                        logt = getStr(item.find('REFINE_WGS84_LOGT').text)
                        lat = getStr(item.find('REFINE_WGS84_LAT').text)
                        building = getStr(item.find('FACLT_NM').text)
                        break
            if(not find_in_dontselect):
                elements = get_xml_swim()
                for item in elements:
                    name = item.find('FACLT_NM').text
                    if name == data[1]:
                        find_in_dontselect = True
                        _text1 = "시설명 : " + getStr(item.find('FACLT_NM').text)
                        _text2 ='시군명 : ' + getStr(item.find('SIGUN_NM').text)
                        _text3 ="도로명 주소 : " + getStr(item.find('REFINE_ROADNM_ADDR').text)
                        _text4 = "연락처 : " + getStr(item.find('CONTCT_NO').text)
                        _text5 = "홈페이지 주소 : " + getStr(item.find('HMPG_ADDR').text)
                        _text6 = "면적(건축) : " + getStr(item.find('BUILD_AR').text) + "m^2"
                        _text7 = getStr(item.find('REFINE_LOTNO_ADDR').text)
                        logt = getStr(item.find('REFINE_WGS84_LOGT').text)
                        lat = getStr(item.find('REFINE_WGS84_LAT').text)
                        building = getStr(item.find('FACLT_NM').text)
                        break
            if(not find_in_dontselect):
                elements = get_xml_inside()
                for item in elements:
                    name = item.find('FACLT_NM').text
                    if name == data[1]:
                        find_in_dontselect = True
                        _text1 = "시설명 : " + getStr(item.find('FACLT_NM').text)
                        _text2 ='시군명 : ' + getStr(item.find('SIGUN_NM').text)
                        _text3 ="도로명 주소 : " + getStr(item.find('REFINE_ROADNM_ADDR').text)
                        _text4 = "연락처 : " + getStr(item.find('CONTCT_NO').text)
                        _text5 = "홈페이지 주소 : " + getStr(item.find('HMPG_ADDR').text)
                        _text6 = "면적(건축) : " + getStr(item.find('BUILD_AR').text) + "m^2"
                        _text7 = getStr(item.find('REFINE_LOTNO_ADDR').text)
                        logt = getStr(item.find('REFINE_WGS84_LOGT').text)
                        lat = getStr(item.find('REFINE_WGS84_LAT').text)
                        building = getStr(item.find('FACLT_NM').text)
                        break
    
        info_listbox.insert(1, _text1)
        info_listbox.insert(2, _text2)
        info_listbox.insert(3, _text3)
        info_listbox.insert(4, _text4)
        info_listbox.insert(5, _text5)
        info_listbox.insert(6, _text6)
        info_listbox.insert(7, logt)
        info_listbox.insert(7, lat)
        print(building)
        print(_text7)
        print(logt)    
        print(lat)

# 농구장 xml
def get_xml_basket():
    from xml.etree import ElementTree

    server = "openapi.gg.go.kr"
    basket_conn = http.client.HTTPSConnection(server)
    basket_conn.request(
            "GET",
            "/PublicLivelihood?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )
    basket_res = basket_conn.getresponse()

    if int(basket_res.status) == 200:
        basket_strXml = basket_res.read().decode('utf-8')
    else:
        print('HTTP request failed : ', basket_res.reason)

    basket_parseData = ElementTree.fromstring(basket_strXml)
    basket_elements = basket_parseData.iter('row')

    return basket_elements

# 축구장 xml
def get_xml_soccer():
    from xml.etree import ElementTree

    server = "openapi.gg.go.kr"
    foot_conn = http.client.HTTPSConnection(server)
    foot_conn.request(
            "GET",
            "/PublicTrainingFacilitySoccer?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )
    foot_res = foot_conn.getresponse()

    if int(foot_res.status) == 200:
        foot_strXml = foot_res.read().decode('utf-8')
    else:
        print('HTTP request failed : ', foot_res.reason)
            
    foot_parseData = ElementTree.fromstring(foot_strXml)
    foot_elements = foot_parseData.iter('row')

    return foot_elements        

# 수영장 xml
def get_xml_swim():
    from xml.etree import ElementTree

    server = "openapi.gg.go.kr"
    swim_conn = http.client.HTTPSConnection(server)
    swim_conn.request(
            "GET",
            "/PublicSwimmingPool?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )
    swim_res = swim_conn.getresponse()

    if int(swim_res.status) == 200:
        swim_strXml = swim_res.read().decode('utf-8')
    else:
        print('HTTP request failed : ', swim_res.reason)
            
    swim_parseData = ElementTree.fromstring(swim_strXml)
    swim_elements = swim_parseData.iter('row')

    return swim_elements

# 실내 스포츠 xml
def get_xml_inside():
    from xml.etree import ElementTree

    server = "openapi.gg.go.kr"

    inside_conn = http.client.HTTPSConnection(server)
    inside_conn.request(
            "GET",
            "/PublicGameOfBallGymnasium?KEY=3cccb5986c79462dae3acd235fa8a54f"
        )
    inside_res = inside_conn.getresponse()

    if int(inside_res.status) == 200:
        inside_strXml = inside_res.read().decode('utf-8')
    else:
        print('HTTP request failed : ', inside_res.reason)
            
    inside_parseData = ElementTree.fromstring(inside_strXml)
    inside_elements = inside_parseData.iter('row')

    return inside_elements


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
    global stateinput
    global s_listbox
    global sport_num

    i = 1

    if sport == "농구장":
        sport_num = "농구"
    elif sport == "축구장":
        sport_num = "축구"
    elif sport == "수영장":
        sport_num = "수영"
    elif sport == "실내스포츠(배드민턴, 탁구)":
        sport_num = "실내"
    else:
        sport_num = "선택안함"


    # 농구 데이터-------------------------------------------------------------
    bs_num = 0

    if(sport == "농구장" or sport == "선택안함"):
        basket_elements = get_xml_basket()
        for item in basket_elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            if stateinput.get() not in part_el.text:
                continue
            _text = '[' + str(i) + ']:' + \
                getStr(item.find('FACLT_NM').text) + \
                ':' + getStr(item.find('SIGUN_NM').text)
            
            bs_num += 1
            s_listbox.insert(i-1,_text)
            i = i+1
    
    # 축구 데이터-------------------------------------------------------------
    ft_num = 0

    if(sport == "축구장" or sport == "선택안함"):
        foot_elements = get_xml_soccer()
        for item in foot_elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            if stateinput.get() not in part_el.text:
                continue
            _text = '[' + str(i) + ']:' + \
                getStr(item.find('FACLT_NM').text) + \
                ':' + getStr(item.find('SIGUN_NM').text)
                
            ft_num += 1

            s_listbox.insert(i-1,_text)
            i = i+1
    
    # 수영 데이터-------------------------------------------------------------
    sw_num = 0

    if(sport == "수영장" or sport == "선택안함"):
        swim_elements = get_xml_swim()

        for item in swim_elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            if stateinput.get() not in part_el.text:
                continue
            _text = '[' + str(i) + ']:' + \
                getStr(item.find('FACLT_NM').text) + \
                ':' + getStr(item.find('SIGUN_NM').text)
                
            sw_num += 1

            s_listbox.insert(i-1,_text)
            i = i+1
    
    # 실내스포츠 데이터-------------------------------------------------------------
    ins_num = 0

    if(sport == "실내스포츠(배드민턴, 탁구)" or sport == "선택안함"):
        inside_elements = get_xml_inside()
        for item in inside_elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            if stateinput.get() not in part_el.text:
                continue
            _text = '[' + str(i) + ']:' + \
                getStr(item.find('FACLT_NM').text) + \
                ':' + getStr(item.find('SIGUN_NM').text)
                
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

# 캔버스 그리기
def drawCanvas():
    global canvas, canvasWidth, canvasHeight

    canvasWidth = 460
    canvasHeight = 250

    canvas = Canvas(root, width=canvasWidth, height=canvasHeight, bg='white')
    
    canvas.place(x=20, y=400)

    canvas.create_rectangle(20, 400, 460, 250, fill='white', tag="graph")


# 그래프 그리는 함수
def drawGraph(sport, data):
    # 그래프 크기는, [left, top, right, bottom] = [20, 400, 480, 650], 가로 = 460px, 세로 = 250px
    global root, canvas, canvasWidth, canvasHeight

    if(sport == "선택안함"):
        canvas.delete("graph")

        nData = len(data)
        nMax = max(data, key=lambda x:x['value'])
        nMin = min(data, key=lambda x:x['value'])

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

            canvas.create_text(left - 20, (top + bottom) // 2, text=data[i]["value"], tag="graph")
            canvas.create_text(right + 20, (top + bottom) // 2, text=data[i]["name"], tag="graph")
    else:
        canvas.delete("graph")


def getStr(s):
    return '' if not s else s

#지도로 이동
def sports_map():
    global location
    global info_listbox
    global _text7
    global logt
    global lat
    global building
    
 
    print(_text7)
    print(logt)
    print(lat)
    location = tkinter.Toplevel()
    location.geometry ("500x600+550+100")
    location.title("지도")
    location.resizable(False, False )
    location_font = tkinter.font.Font(family = "나눔 고딕" , size = 15)
    location_text= tkinter.Label(location, text = "[지도]", font = location_font)
    location_text.pack()
    
    map_widget =  tkintermapview.TkinterMapView(location, width=800, height=500, corner_radius=0)
    map_widget.pack()
    map_widget.set_position(float(lat), float(logt))

    # marker_1 = map_widget.set_address("경기도 시흥시 산기대학로 237", marker=True)
    # print(marker_1.position, marker_1.text)# get position and text
    # marker_1.set_text("한국공학대학교") # set new text
    marker_1 = map_widget.set_address(_text7 , marker=True)
    print(marker_1.position, marker_1.text)
    marker_1.set_text(building)
    map_widget.set_zoom(15)



#이메일 보내기
def Send_email():
    global mail
    global mailinput
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
    SearchButton = Button(mail, font = s_mail_font, text="전송", command=partial(sendMail) )
    SearchButton.pack()



# 이메일 보내기
def sendMail():
    global senderAddr
    global recipientAddr
    global msg 
    global mailinput
    global mail
    global info_listbox
    
    senderAddr = "doyoung930@gmail.com"
    recipientAddr = mailinput.get()

    body =info_listbox.get(0)+"\n"+ info_listbox.get(1) +"\n" + info_listbox.get(2)+"\n" + info_listbox.get(3)+"\n" + info_listbox.get(4)+"\n"+ info_listbox.get(5)+"\n"+ info_listbox.get(6)
    msg = MIMEText(body)
    msg['Subject'] = "체육시설 정보"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr


    import smtplib # 파이썬의 SMTP 모듈
# 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) 
# SMTP 서버와 연결
    s.starttls() 
# 앱 password 이용
    s.login('doyoung930@gmail.com', 'rjsqqhispyapkuwc')
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
    mail.destroy()
    messagebox.showinfo("메일", "메일이 성공적으로 보내졌습니다.")

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