class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
def test_person():
    p = Person(1, "홍길동")
    assert p.id == 1
    assert p.name == "홍길동"

def test_person_printInfo(capsys):
    p = Person(2, "김철수")
    p.printInfo()
    captured = capsys.readouterr()
    assert "ID: 2, Name: 김철수" in captured.out

def test_manager():
    m = Manager(3, "이영희", "팀장")
    assert m.id == 3
    assert m.name == "이영희"
    assert m.title == "팀장"

def test_manager_printInfo(capsys):
    m = Manager(4, "박민수", "부장")
    m.printInfo()
    captured = capsys.readouterr()
    assert "ID: 4, Name: 박민수, Title: 부장" in captured.out

def test_employee():
    e = Employee(5, "최지훈", "Python")
    assert e.id == 5
    assert e.name == "최지훈"
    assert e.skill == "Python"

def test_employee_printInfo(capsys):
    e = Employee(6, "정수빈", "Java")
    e.printInfo()
    captured = capsys.readouterr()
    assert "ID: 6, Name: 정수빈, Skill: Java" in captured.out

def test_manager_is_person():
    m = Manager(7, "오세훈", "과장")
    assert isinstance(m, Person)

def test_employee_is_person():
    e = Employee(8, "김유진", "C++")
    assert isinstance(e, Person)

def test_manager_override():
    m = Manager(9, "이준호", "사장")
    assert hasattr(m, "printInfo")

def test_employee_override():
    e = Employee(10, "박지민", "Go")
    assert hasattr(e, "printInfo")