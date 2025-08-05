strName = "Not Class Member"

class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        # 전역변수
        print(strName)
        # 지역변수
        print(self.strName)
d = DemoString()
d.set("First Message")
d.print()
