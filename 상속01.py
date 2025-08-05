class Person:
    def __init__(self, name, phoneNumber):
        # 부모의 초기화 메서드 호출
        super().__init__(name, phoneNumber)
        self.name = name
        self.phoneNumber = phoneNumber
        # 덮어쓰기
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, 
            self.phoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        self.name = name
        self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "24001")
print(p.__dict__)
print(s.__dict__)


