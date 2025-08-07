# demoDict.py 
print("---형식 변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(10)
print(b)
c = tuple(b)
print(c)

print("---dict---")
colors = {"apple":"red", "banana":"yellow"}
#입력
colors["cherry"] = "red"
print(colors)
#검색
print(colors["apple"])
#삭제
del colors["apple"]
print(colors)

#장비모음
device = {"아이폰":5, "아이패드":10, "윈도우타블렛":15}
#입력 
device["맥북"] = 20 
print(device)
#수정
device["아이폰"] = 6 
print(device)
#삭제
del device["맥북"]
#반복문
for item in device.items():
    print(item)

for k,v in device.items():
    print(k, v)
    