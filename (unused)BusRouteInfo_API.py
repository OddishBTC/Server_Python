# Python3 샘플 코드 #
# https://open.jejudatahub.net/api/proxy/aaatD6D1atta1611at1t6a1b6at1b11a/{your_projectKey}?{params(key=value)}

import requests
import json
import pandas as pd

def callAPI():
    url = 'https://open.jejudatahub.net/api/proxy/aaatD6D1atta1611at1t6a1b6at1b11a/'
    your_projectKey = 'rpte41c1br__11cp1c4etctc_t1_p1j7'
    
        
    # params ={'number' : '8', 'limit' : '100'}
    
    # response = requests.get(url+your_projectKey, params=params)
    # print(response.content)
    
    busRouteNum = []
    
    for i in range(1,9):
        params ={'number' : str(i), 'limit' : '100'}
        response = requests.get(url+your_projectKey, params=params)
        res_json = json.loads(response.content)
        res_json_data = res_json['data']
        for index in res_json_data:
            busRouteNum.append(index['routeNumber'])
            
    return busRouteNum        


def save_csv():   
    bRML = callAPI()
    busRouteNumList = list(set(bRML))
    busRouteNumList.sort()
    
    df = pd.DataFrame(busRouteNumList, columns=['Num'])
    df.to_csv('BusRouteNumList.csv')
    return


def main():
    save_csv()


if __name__ == '__main__':
     main()
