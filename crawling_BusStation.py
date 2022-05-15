# 참고 : https://www.selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/firefox.html
# 참고 : https://selenium-python.readthedocs.io/index.html
# 참고 : 파이썬 빅데이터분석 책
# 참고 : https://catloaf.tistory.com/19


#<input class="btn_time" type="text" placeholder="Enter route numbers" value="" title="Enter route numbers">
#/html/body/div/div[3]/div/div[1]/input




from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time


def convertColRow(string):
    df = pd.DataFrame(string)
    df = df.transpose()
    #df = df.drop(df.index[0], axis=0)   #행 삭제
    #df = df.drop(df.index[0], axis=1)   #열 삭제
    return df


def save_csv(string, file_name):       
    df = pd.DataFrame(string)
    df.to_csv("BusRouteNumList/"+file_name+".csv")
    return
    

def crawling():
    jejubusinfo_URL = "https://bus.jeju.go.kr/search/line#"
    wd = webdriver.Firefox()
    wd.get(jejubusinfo_URL)
    time.sleep(4)  #웹페이지 연결할 동안 3초 대기
    
    df = pd.read_csv('BusRouteNumList.csv')
    
    busNum = list(df['0'])

    for i in busNum:
        element = wd.find_element_by_class_name("btn_time")
        time.sleep(1)  #스크립트 실행 할 동안 1초 대기    
        element.send_keys(i)
        time.sleep(1)  #스크립트 실행 할 동안 1초 대기    
        wd.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/a").click()
        time.sleep(1)  #스크립트 실행 할 동안 1초 대기    
        
        
        # -----------------------#
        # 각 경로 목록들을 구하기 #
        # ---------------------- #
        try:
            for j in range(2,30):
                wd.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[3]/div/ul/li[%d]/div"%j).click() #버스 운행 경로 목록 중 하나씩 선택
                time.sleep(1) #스크립트 실행 할 동안 1초 대기                

                # ------------------------------------------- 버스 이름 구하기 ---------------------------------------------
                soupCB = BeautifulSoup(html, 'html.parser')
                html = wd.page_source    # html 따오기
                bus_name = soupCB.select("p.item")      # 버스 경로 정보 따오기
                
                busName = ''
                tmp = 0
                for k in bus_name:
                    busName = busName + str(bus_name[tmp].contents)
                    tmp = tmp + 1
                
                busName = busName.replace("['",'')
                busName = busName.replace("']",'')
                busName = busName[4:]
                busName = busName.replace(" ",'')
                #print(busName)  #버스 이름 출력하기
                
                
                # ------------------------------------------- 모든 정류소 구하기 ---------------------------------------------
                # html = wd.page_source    # html 따오기
                # soupCB = BeautifulSoup(html, 'html.parser')
                bus_Route = soupCB.select("p.station_text")      # 버스 모든 정류소 정보 따오기
                busRoute = ''
                tmp = 0
                for k in bus_Route:
                    busRoute = busRoute + str(bus_Route[tmp].contents)[1:-1]
                    tmp = tmp + 1

                busRoute = busRoute[1:-1]
                busRoute = busRoute.split("''")
                #print(busRoute)  #버스 경로 출력하기
                
                save_csv(convertColRow(busRoute), i+'/'+busName)
                # str(i)+'/'+busName
                
                wd.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[3]/div/ul/li/div").click() #목록 선택 화면으로 돌아감
                
        except:
            wd.refresh()
            time.sleep(4)  #웹페이지 연결할 동안 3초 대기
            continue
    
    return


def main():
    crawling()
    return
   
    
if __name__ == '__main__':
    main()




# def tmpBusNumList():
#     # ------------------------#
#     # 대략적인 버스 번호 목록들 #
#     # ------------------------#
#     tmpBusNumList = [43,600,800,810,820,880,900,910,921,922,924,1111]
#     tmpBusNumList = tmpBusNumList + list(range(101,183)) + list(range(201,296)) + list(range(300,381)) + list(range(411,491))
#     tmpBusNumList = tmpBusNumList + list(range(510,533)) + list(range(611,693)) + list(range(701,796))
#     tmpBusNumList = tmpBusNumList + list(range(3001,3009)) + list(range(5001,5007))
#     tmpBusNumList.sort()
#     return tmpBusNumList