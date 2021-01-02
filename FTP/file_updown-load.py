# FTP protocol을 이용한 파일 다운/업로드 프로그램

from ftplib import FTP
import os

print("FTP 통신을 통해 서버와 클라이언트의 프로그램을 다운/업로드하는 프로그램을 시작합니다.")

try:
    IP = input("사용자의 IP 주소를 입력해주세요: ")
    ftp = FTP(IP)
except:
    print("잘못된 입력 형식입니다.")

print('banner: ', ftp.getwelcome())
print('login: ', ftp.login())
print('pwd: ', ftp.pwd())
print('List: ', ftp.retrlines('LIST'))

print("\n###\n1.파일 다운\n2.파일 업로드\n3.프로그램 종료")
temp = int(input("1 or 2 or 3 : "))
while(temp == 1 or temp == 2):
    if temp == 1:
        df = input("다운할 파일 이름을 입력해주세요\n ex)@.txt : ")
        df2 = input("다운한 파일을 저장할 이름을 입력해주세요\n ex)@.txt : ")
        try:
            print('=> RETR: ', ftp.retrbinary('RETR '+df,
                                              open(''+df2, 'wb').write))
        except:
            print("잘못된 입력형식이거나 파일의 위치가 잘못되었습니다.")

        print("\n###\n1.파일 다운\n2.파일 업로드\n3.프로그램 종료")
        temp = int(input("1 or 2 or 3 : "))

    elif temp == 2:
        print("$$$$$ 파이썬 실행 파일과 동일한 위치에 업로드할 파일이 존재해야 합니다.$$$$$")
        df = input("업로드할 파일 이름을 입력해주세요\n ex)@.txt :  ")
        df2 = input("업로드한 파일을 저장할 이름을 입력해주세요\n ex)@.txt : ")
        try:
            print('=> STOR: ', ftp.storbinary('STOR '+df,
                                              open(''+df2, 'rb')))
        except:
            print("잘못된 입력형식이거나 파일의 위치가 잘못되었습니다.")

        print("\n###\n1.파일 다운\n2.파일 업로드\n3.프로그램 종료")
        temp = int(input("1 or 2 or 3 : "))

print("\n===\n프로그램을 종료합니다.\n")
