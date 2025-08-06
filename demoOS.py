#demoOS.py

from os.path import *

fName = "sample.txt"
print(abspath(fName))
print(basename(r"c:\work\text.t"))

if (exists(r"c:\python310\python.exe")):
    print(getsize(r"c:\pyton310\"Python exists"))
else
    print("파일이 없음")

print("운영체제명:", name)
print("환경변수:", environ)
system("notepad.exe")

print(glob.glob(*.py))

