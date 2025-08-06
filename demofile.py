#demofile.py
#블럭을 선택하고 주석처리 : ctr + /
#파일쓰기
#f = open("c:\\work\\test.txt", "w", encoding="utf-8")
#f.write("첫번째\n두번째\n세번째\n")
#f.close()

#파일읽기(raw string natation)
#f = open(r"c:\work\test.txt", "rt", encoding="utf-8")
#print(f.read())
#f.close()


#문자열처리
strA = "파이썬은 강력해"
strB = "Python is powerful"
print(len(strA))  # 문자열 길이
print(len(strB))
print(strA.capitalize())
print(strB.upper)  # 대문자
print(strB.lower())  # 소문자
print(strA.replace("강력해", "재미있어"))  # 문자열 치환
print("MBC2580".isalnum())  # 영문자와 숫자로만 구성되어 있는지 확인
print("2580".isdecimal())
data = "<<< spam and ham   >>>" 
result = data.strip("<> ")  # 양쪽 공백과 특정 문자 제거
print(data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)  # 문자열 치환   
lst = result2.split()  # 문자열 분리
print(lst)  # ['spam', 'egg', 'and', 'ham']
print(":".join(lst))  # 리스트를 문자열로 합치기

#정규표현식
import re
result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())  # 검색된 문자열 출력

# 선택한 것 전체를 주석표시 : ctr+/
# result = re.match("[0-9]*th", "35th")
# print(result)
# print(result.group())  # '35th'

result = re.search("apple", "this is apple")
print(result.group())  # 'apple'

result = re.search(r"\d{4}", "올해는 2025년입니다.")
print(result.group())  # 'apple'

result = re.search(r"\d{5}", "우리 동네는 51200입니다.")
print(result.group())  # 'apple'
