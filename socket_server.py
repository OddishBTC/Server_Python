import re
import socket
import threading
# 주최자
# host = '127.0.0.1'
host = '192.168.1.6'
# 포트
port = 9000

class Server:
    def __init__(self, host_addr='127.0.0.1', port=6667):
        self.host_addr = host_addr
        self.port = port
        self.sock = None
        self.addr = None

    def init(self):
        try:
            # 소켓 개체 인스턴스를 만듭니다  socket.AF_INET은 IPV4 및 기타 네트워크 유형을 기반으로 하는 소켓 제품군을 나타내고 socket.SOCK_STREAM은 연결 지향적이고 안정적인 데이터 전송 서비스를 제공하는 데 사용되는 스트림 소켓을 나타냅니다
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 주소(호스트, 포트)를 소켓에 바인드
            self.sock.bind((self.host_addr, self.port))
            # TCP 모니터링 수행, 10은 만들 수 있는 최대 연결 수를 나타냅니다
            self.sock.listen(10)
        except socket.error as e:
            print(e)
            exit()
        print("서버가 성공적으로 초기화되었으며 연결을 기다리는 중")

    def accept_client(self):
        # 클라이언트가 연결하기를 기다리는 중
        while True:
            conn, addr = self.sock.accept()
            self.addr = addr
            print("클라이언트 IP：{}연결된,항구는:{}！".format(self.addr[0],self.addr[1]))
            # 자식 스레드 개체를 만들고 매개 변수를 전달하고 함수를 처리합니다
            t = threading.Thread(target=self.handle_message, args=(conn,))
            t.setDaemon(True)
            t.start()
    
    # 클라이언트 데이터를 수락하기 위해
    def handle_message(self, client):
        client.send('서버에 성공적으로 연결되었습니다！'.encode('utf-8'))
        try:
          while True:
            # 클라이언트 데이터 수락
            data = client.recv(1024).decode('utf-8').strip()
            if data:
                print(data)
                client.send('456'.encode('utf-8'))
        except Exception as e:
            print(e)

    def main(self):
        # 초기화
        self.init()
        # 듣기 시작
        self.accept_client()

if __name__ == '__main__':
    s = Server('192.168.1.6', 9000)
    s.main()
    