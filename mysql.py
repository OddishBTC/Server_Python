import pymysql


class Connect_mysql:
    def __init__(self,
                 host='127.0.0.1',
                 username='root',
                 password='123456',
                 db='test'):
        self.host = host
        self.port = 3306
        self.username = username
        self.password = password
        self.db = db
        self.con = None
        self.connect_mysql()

    def connect_mysql(self):
        # 데이터베이스 ip, 포트 번호, 사용자 이름, 암호 연결
        try:
            self.con = pymysql.connect(host=self.host,
                                       port=3306,
                                       user=self.username,
                                       password=self.password,
                                       db=self.db,
                                       charset='utf8')
        except Exception as e:
            print(e)
            print('데이터베이스 연결 실패')
            exit()

    def execute(self, sql):
        # 커서 
        cursor = self.con.cursor()
        # SQL 문을 실행
        cursor.execute(sql)
        # 데이터 반환
        r = cursor.fetchall()
        # 데이터 제출
        self.con.commit()
        return r

    # 데이터베이스 test_table 테이블 생성
    def create(self):
        # 데이터 테이블 생성 sql 명령
        sql = ' CREATE TABLE test_table (id INT(11) AUTO_INCREMENT,name VARCHAR(25),occupation INT(11),salary FLOAT,PRIMARY KEY (id));'
        self.execute(sql)
        print('데이터베이스를 성공적으로 생성')

    # 데이터 추가
    def add(self, name, occupation, salary):
        # 데이터 추가 SQL 명령
        sql = """insert into test_table (name, occupation, salary) VALUES ('{}','{}','{}')""".format(name, occupation, salary)
        print("""add data (name, occupation, salary) :('{}','{}','{}')""".format(name, occupation, salary))
        self.execute(sql)

    # 데이터 삭제
    def delete(self, name):
        # 데이터 삭제 SQL 명령
        sql = """ DELETE FROM test_table WHERE name='{}'""".format(name)
        print("""delete data (name) :('{}')""".format(name))
        self.execute(sql)

    # 데이터 업데이트
    def update(self, name, occupation, salary):
        # 데이터 업데이트 SQL 명령
        sql = """UPDATE test_table SET occupation='{}', salary='{}' where name='{}'""".format(name, occupation, salary)
        print(f'update data {name},{occupation},{salary}')
        self.execute(sql)
        
    # 검색 데이터
    def search(self):
        # 데이터 검색 SQL 명령
        sql = """select * from test_table;"""
        recv = self.execute(sql)
        if recv:
            for i in recv:
                print("""id:{}, name:{}, occupation:{}, salary:{} """.format(i[0], i[1], i[2],i[3]))
    # 파괴하다
    def __del__(self):
        if self.con:
            self.con.close()


if __name__ == '__main__':
    # 인스턴스화된 객체
    mysql = Connect_mysql()
    # 루프 추가 데이터
    # for i in range(10):
    #     mysql.add('user'+str(i),i,i**2)
    # mysql.search()
    # mysql.update('user1', 'student', 10)
    # mysql.search()
    for i in range(10):
        mysql.delete('user'+str(i))
    # mysql.search()
    
