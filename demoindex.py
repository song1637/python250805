# demoindes.py

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))
print(strA[:2])
print(strB[:6])
print(strB[-3:])

strC = """이번에는
다중의 라인을
저장합니다."""

print(strC)


print("---리스트형식---")
lst = [10, 20, 30]
print(len(lst))
print(lst)
lst.append(40)
print(lst)
lst.insert(1,5)
print(lst)
lst.insert(2,6)
print(lst)
lst.remove(20)
print(lst)


print("---Tuple---")
tp =(100, 200, 300)
print(len(tp))
print(tp[1])
print(tp.index(300))

# 함수를 정의
def calc(a,b):
    return a+b, a*b

# 함수를 호출
print(calc(3,4))

print("id: %s, name:%s" %("Kim","김유신"))
      
args = (5,6)
print(calc(*args))

print("---set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
b = list(a)
print(b)
b = tuple(a)
print(b)