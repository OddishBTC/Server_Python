# 참고 (Python에서 디렉터리의 모든 파일 열기) :https://www.delftstack.com/ko/howto/python/python-open-all-files-in-directory/

import os
import pandas as pd

def openFile():
    files = "JejuBusTime/All_converted"
    for filename in os.listdir(files):
        df = pd.read_csv(files+"/"+filename)
        try:
            if df.loc[5,'Unnamed: 2'] == "노선번호":
                BusSet = set(df.loc[:,'Unnamed: 2'])
                print(BusSet)
        except:
            continue
        

def main():
    openFile()

    return
   
    
if __name__ == '__main__':
    main()


















# import os
# import pandas as pd

# def openFile(list):
#     for i in list:
#         files = "BusRouteNumList/"+i
#         for filename in os.listdir(files):
#             df = pd.read_csv(files+"/"+filename)
#             print(df)
#            # with open(os.path.join(files, filename), 'r') as f:
#            #     text = f.read()
#            #     print(text)



# def main():
#     df = pd.read_csv('BusRouteNumList.csv')
#     busNum = list(df['0'])

#     openFile(busNum)

#     return
   
    
# if __name__ == '__main__':
#     main()