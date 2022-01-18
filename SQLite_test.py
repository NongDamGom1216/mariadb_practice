#python SQLite로 db관리하는 법(maridDB 아님)

import sqlite3

def main():
    #db 접속관리
    con = sqlite3.connect('addr.db') #DB파일이 없으면 새로 생성
    print('db 연결 성공')

    cursor = con.cursor() # SQL 실행

    cursor.execute("SELECT * FROM tblAddr") # 메모리에 저장

    table = cursor.fetchall() # 메모리에 저장된 값의 모든 데이터를 꺼내서 컬렉션으로 return
    print(type(table))
    print(type(table[0])) # 개별 타입 확인
    print(table[0])

    for record in table:
        print(f'이름: {record[0]}, 번호: {record[1]}, 주소: {record[2]}')
    
    cursor.close()
    con.close()

main()