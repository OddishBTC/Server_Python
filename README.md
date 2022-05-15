# Server_Python
Crawling and Parsing Bus Information System + Save Information


### 0.1 제주버스시간.zip
> 제주버스정보시스템에 직접 다운로드받은 버스시간표 excel 파일(.xlsx) 첨부.
> **(2022.04.08 에 다운로드 받음) (제주버스정보시스템 공지사항을 참고하여, 수정되는 버스시간표가 있을 시 업데이트를 해줘야 함.)**

### 0.2 결과물.zip
> 현재까지 진행하여 얻은 결과물 -> 아래 파이썬 코드들을 실행해서 얻은 결과물들


## 1. (unused)BusRouteInfo_API.py
> 우선 제주데이터허브의 버스 노선 정보 API를 불러와서 BusRouteNumList.csv 파일을 저장했음. 근데 정보가 부적합하다고 판단하여 2번에서 수정작업을 좀 했음

## 2. BusRouteNumList.py
> 부족한 버스 노선 정보를 직접 추가하는 작업을 했음. 그리고 수정한 데이터를 BusRouteNumList.csv 파일로 저장함.

## 3. convert_to_csv.py
> 제주버스정보시스템에서 직접 다운로드받은 excel(.xlsx) 파일을 .csv 파일로 변환하는 작업을 함.
> **+ 근데 데이터프레임을 깔끔하게 정리하는 수정 작업이 필요할 것 같음**

## 4. BusRoutNumList_CreateFolders.py
> 버스 노선에 따른 각각의 폴더들을 만드는 작업. 이 폴더 안에 5번에서 크롤링한 csv파일들을 저장할 것임.

## 5. crawling_BusStation.py
> 제주버스정보시스템 사이트를 동적 크롤링함.
> **+ 코드를 실행해도 빼먹는 노선들이 좀 있기 때문에 코드를 충분히 여러번 실행할 필요 있음.**

## 6. csv_parsing(unfinished).py
> 5번에서 크롤링한 것을 적당히 잘 파싱하고 정리하는 것.
> **+ 아직 미완성. 작업 중. **
