import sys
import telepot
from pprint import pprint # 데이터를 읽기 쉽게 출력
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString
import http.client

TOKEN = '5417445912:AAEFLuMDXHx9iuKGljqr7vsH6XI3pLszj4Q'
MAX_MSG_LENGTH = 300

server = "openapi.gg.go.kr"

bot = telepot.Bot(TOKEN)

def getData(loc_param, sport_param): 
    res_list = []

    if sport_param == "농구":
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
        elements = basket_parseData.iter('row')
    elif sport_param == "축구":
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
        elements = foot_parseData.iter('row')
    elif sport_param == "수영":
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
        elements = swim_parseData.iter('row')
    elif sport_param == "실내":
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
        elements = inside_parseData.iter('row')

    for item in elements:
        txt_y, nm, y, n, addr = '', '', '', '', ''
        if loc_param == item.find("SIGUN_NM").text:
            if item.find("SUM_YY").text != None:
                txt_y = item.find("SUM_YY").text
            if item.find("FACLT_NM").text != None:
                nm = item.find("FACLT_NM").text
            if item.find("COMPLTN_YY").text != None:
                y = item.find("COMPLTN_YY").text
            if item.find("BUILD_AR").text != None:
                n = item.find("BUILD_AR").text
            if item.find("REFINE_LOTNO_ADDR").text != None:
                addr = item.find("REFINE_LOTNO_ADDR").text

            row = txt_y + " // " + nm + '(' + y + ') ' + n + "m²\n" +\
                "지번주소 : " + addr + '\n'

            res_list.append(row)
    
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        # 예외 정보와 스택 트레이스 항목을 인쇄.
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)