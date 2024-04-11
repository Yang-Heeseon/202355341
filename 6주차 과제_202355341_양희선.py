#1번 답
# 입력과 관련된 함수 : input(), read(), readline(), readlines()
# 출력과 관련된 함수 : print(), write(), writeline()

#2번 답 : 1번 A(파일 열기) - C(파일 읽기) - B(파일 쓰기) - D(파일 닫기)


# 3번 답 : 1번, 3번

#4
inFp = open("C:/Temp/data1.txt", "r")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()

#6
inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
