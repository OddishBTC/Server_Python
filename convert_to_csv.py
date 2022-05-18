# 참고 : https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html?highlight=read_excel
# 참고 : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv
# 참고 : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truncate.html#pandas.DataFrame.truncate

import pandas as pd
from pathlib import Path


# file_route = '//home/koh/SWCapstone/JejuBusTime/마을/(동복리)/origin/bus (%d).xlsx' % (2)
# df = pd.read_excel(file_route, sheet_name=0, engine='openpyxl')

# converted_name = '/home/koh/SWCapstone/JejuBusTime/마을/(동복리)/converted_csv/' + df.iloc[0,1] + ", " + df.iloc[1,1] + ".csv"
# filepath = Path(converted_name)
# filepath.parent.mkdir(parents=True, exist_ok=True)
# df.to_csv(filepath)

def convert(relative_route):
    x=1
    i=0
    breaker=0
    
    while True:
        file_route = relative_route + '/origin/bus (%d).xlsx' % (x)

        while True:
            try:
                df = pd.read_excel(file_route, sheet_name=i, engine='openpyxl')
                
                a = df.iloc[0,1]
                b = df.iloc[1,1]
                
                if a.find('/'):
                    a = a.replace('/',',')
                
                if b.find('/'):
                    b = b.replace('/',',')
                
                converted_name = relative_route + "/converted_csv/" + a + ", " + b + ".csv"
                filepath = Path(converted_name)
                filepath.parent.mkdir(parents=True, exist_ok=True)
                
                df = df.drop('Unnamed: 0', axis=1)
                dataF = df.truncate(before=5, axis=0)
                dataF = dataF.rename(columns=dataF.iloc[0])    # 첫번째 행을 column으로지정
                dataF = dataF.drop([5])    # 첫번째 행을 삭제한다                분
                dataF = dataF.set_index('구분')
                dataF.to_csv(filepath)
                
                i=i+1
            
            except ValueError:
                i=0
                break
            
            except FileNotFoundError:
                x=1
                breaker=1
                break
            
        x=x+1
        
        if breaker==1:
            breaker=0
            print("finish!")
            break
        
    return

def main():
    convert('JejuBusTime/간,지선+저상+관광지순환')
    convert('JejuBusTime/공항리무진')
    convert('JejuBusTime/급행')
    convert('JejuBusTime/마을/(동복리)')
    convert('JejuBusTime/마을/(추자,우도)')
    convert('JejuBusTime/시티투어(정보모름)')
    return
    
if __name__ == '__main__':
     main()

