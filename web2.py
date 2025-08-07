# web2.py 
from bs4 import BeautifulSoup
import urllib.request
import re 

#파일로 저장
f = open('clien.txt', 'wt', encoding='utf-8')
#페이징 처리(번호를 생성)
for i in range(0,10):
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)  
    print(url)
    #함수 체인(메서드 체인)
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    for tag in soup.find_all('span', attrs={'data-role':'list-title-text'}):
        title = tag.text.strip()
        if re.search('아이패드', title):
            print(title)
            f.write(title + '\n')

f.close()

    # <span class="subject_fixed" data-role="list-title-text" title="아이폰 13미니 256 팝니다">
    #     아이폰 13미니 256 팝니다
    # </span>