import pandas as pd
# from pathlib import Path

# 파이썬으로 폴더 생성하기 - 출처: https://data-make.tistory.com/170 [Data Makes Our Future]

import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def createFolder_BusRouteNumList():

    df = pd.read_csv('BusRouteNumList.csv')
    
    busNum = list(df['0'])
    
    for i in busNum:
        createFolder('BusRouteNumList/'+i)



def main():
    createFolder_BusRouteNumList()
    return
    
if __name__ == '__main__':
      main()

