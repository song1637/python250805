# db1.py
import sqlite3

#연결객체를 리턴
# con = sqlite3.connect(":memory:")
con = sqlite3.connect(r"c:\work\sample.db")
#커서객체를 리턴
cur = con.cursor() 
#테이블 생성
cur.execute("create table Phonebook (name text, phone text);")
#데이터 삽입
cur.execute("insert into Phonebook values ('홍길동', '123-456');")
#입력 파라메터 처리
name = '이순신'
phone = '987-654'
cur.execute("insert into Phonebook values (?, ?);", (name, phone))
#여러건 입력
datalist = [('강감찬', '111-222'), ('유관순', '333-444')]
cur.executemany("insert into Phonebook values (?, ?);", datalist)

#데이터 조회    
cur.execute("select * from Phonebook;")
for row in cur: 
    print(row)

#작업을 정상적으로 종료
con.commit()
