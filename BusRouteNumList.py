import pandas as pd

df = pd.read_csv('BusRouteNumList.csv')

data = list(df['Num'])
missData = ['910','921','922','924','1111','202-1','202-2','320-1','356-1','423','424','453','454','623','624','743','744','795','820-3']

data = data + missData

data.sort()

BusData = pd.DataFrame(data)

BusData.to_csv('BusRouteNumList.csv')