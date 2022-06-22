# 참고 (Python에서 디렉터리의 모든 파일 열기) : https://www.delftstack.com/ko/howto/python/python-open-all-files-in-directory/



import os
import pandas as pd



# def stackRoutes(stack, df):
#     busRoute = list(df.iloc[0])    # 첫번째 행 - 버스 노선 추출
#     busRoute.remove(0)
#     if stack != None:
#         for station in stack:
#             if station in busRoute: # 기존것과 겹치는 정류장이 있으면 추가하지 않음
#                 continue
#             else:
#                 busRoute.append(station)
#         #busRoute = stack+busRoute
    
#     return busRoute



def loadSchedule(df):
    # 필요없는 열 제거 과정
    df = df.drop(list(df)[0], axis=1)
    for column in df:
        del_col = True
        dataF = df.loc[:, [column]]
        dataF = dataF.transpose()   # 행열 변환
        dataF = dataF.rename(columns=dataF.iloc[0])    # 첫번째 행을 column으로지정
        
        # 한 열의 모든 리스트가 'X'만 포함할 때, 그 열 삭제
        for column2 in dataF:
            if column2!='X':
                del_col = False
                break
        
        if del_col == True:
            df = df.drop([column], axis=1)
        
    return df



def main():
    files = "BusSchedule"
    for filename1 in os.listdir(files):
        
        #stack = None
        for filename2 in os.listdir(files+"/"+filename1):
            df = pd.read_csv(files+"/"+filename1+"/"+filename2)
            print(filename1)
            dF = loadSchedule(df)
            
            # stack = stackRoutes(stack, df)
        #print(stack)
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