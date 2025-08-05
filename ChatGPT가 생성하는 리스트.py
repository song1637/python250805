# 파이썬의 주요 컬렉션 형식 비교: List, Set, Dict, Tuple

# List: 순서가 있고, 중복 허용, 변경 가능
my_list = [1, 2, 2, 3]
print("List:", my_list)
print("List - 인덱싱:", my_list[0])
my_list.append(4)
print("List - 추가 후:", my_list)

# Set: 순서 없고, 중복 불허, 변경 가능
my_set = {1, 2, 2, 3}
print("\nSet:", my_set)  # 중복된 2는 하나만 유지
my_set.add(4)
print("Set - 추가 후:", my_set)

# Dict: 키-값 쌍, 순서 있음 (Python 3.7+), 키는 중복 불가
my_dict = {'a': 1, 'b': 2, 'a': 3}
print("\nDict:", my_dict)  # 키 'a'는 마지막 값으로 덮어씀
print("Dict - 특정 키 조회:", my_dict['a'])
my_dict['c'] = 4
print("Dict - 새 키 추가 후:", my_dict)

# Tuple: 순서 있고, 변경 불가, 중복 허용
my_tuple = (1, 2, 2, 3)
print("\nTuple:", my_tuple)
print("Tuple - 인덱싱:", my_tuple[0])
# my_tuple[0] = 10  # 오류 발생 (주석 해제 시 에러 발생)

# 요약 비교
print("\n--- 요약 비교 ---")
print("자료형\t\t| 순서 보존\t| 중복 허용\t| 변경 가능")
print("List\t\t| O\t\t| O\t\t| O")
print("Set\t\t| X\t\t| X\t\t| O")
print("Dict\t\t| O\t\t| 키 X\t\t| O")
print("Tuple\t\t| O\t\t| O\t\t| X")
