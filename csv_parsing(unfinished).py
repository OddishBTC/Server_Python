# 참고 (Python에서 디렉터리의 모든 파일 열기) : https://www.delftstack.com/ko/howto/python/python-open-all-files-in-directory/
# 참고 (Dataframe 열 분할) : https://www.delftstack.com/ko/howto/python-pandas/split-pandas-dataframe/


import os
import pandas as pd



def simplizeDF(df):
    # excel파일에서 시간표만 따오기
    savedBusNum = df.loc[0,'Unnamed: 1']
    
    df = df.drop(['Unnamed: 0','Unnamed: 0.1'], axis=1)
    dataF = df.truncate(before=5, axis=0)
    dataF = dataF.rename(columns=dataF.iloc[0])    # 첫번째 행을 column으로지정
    dataF = dataF.drop([5])    # 첫번째 행을 삭제한다
    dataF = dataF.set_index('구분')

    return dataF, savedBusNum



def parseNumFile(df, filename, savedBusNum):
    df_col = df.columns    # 경로 따기 (etc: 구분-노선번호-제주대-...)
    
    try:
        # 43-1, 43-2 같이 다른노선이 같은시간표에 있는것을 나누는작업
        if df_col[0] == '노선번호':
            BusSet = set(df.loc[:,'노선번호'])    # 일단 버스번호 리스트 저장
            
            for i in BusSet:
                # 노선분할
                groups = df.groupby(df.노선번호)
                parsedNum_df = groups.get_group(i)
                
                # 필요없는 열(노선번호) 지우기
                parsedNum_df = parsedNum_df.drop(['노선번호'], axis=1)    # 열 지우는 코드
                parsedNum_df = parsedNum_df.reset_index(drop=True)    # index 정리                
                # print(parsedNum_df)
                
                
                # '번'글자 지우고 각 파일에 저장
                if type(str(i)[-1]) == str:
                    i = i.replace('번','')
                    i = i.replace('(평일)','')
                    i = i.replace('(토.공휴일)','동절기')
                    i = i.replace('(토,공휴일)','')
                    i = i.replace('(공항리무진)','')
                    i = i.replace('(임시노선)','')
                parsedNum_df.to_csv('BusSchedule/'+str(i)+'/'+filename)
                #print(i)
        
        
        # 181 같이 단일 노선시간표인것은 그냥 각 파일에 저장  
        else:
            # '번'글자 지우고 각 파일에 저장
            if type(savedBusNum[-1]) == str:
                savedBusNum = savedBusNum.replace('번','')
                savedBusNum = savedBusNum.replace('(평일)','')
                savedBusNum = savedBusNum.replace('(토.공휴일)','')
                savedBusNum = savedBusNum.replace('(토,공휴일)','')
                savedBusNum = savedBusNum.replace('(공항리무진)','')
                savedBusNum = savedBusNum.replace('(임시노선)','')
                savedBusNum = savedBusNum.replace('임시 ','')
                savedBusNum = savedBusNum.replace('\n(변경없음)','')
                df.to_csv('BusSchedule/'+str(savedBusNum)+'/'+filename)
                #rint(savedBusNum)
                
            else:
                df.to_csv('BusSchedule/'+str(savedBusNum)+'/'+filename)
                #print(savedBusNum)
    
    except:
        print(savedBusNum)
        pass


    
def main():
    files = "JejuBusTime/All_converted"
    for filename in os.listdir(files):
        df = pd.read_csv(files+"/"+filename)
        
        df, savedBusNum = simplizeDF(df)
        parseNumFile(df, filename, savedBusNum)

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