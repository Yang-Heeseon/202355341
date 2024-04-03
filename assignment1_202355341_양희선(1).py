#5
ss = "Python"

for i in range(0, len(ss)) :
    print(ss[i] + "$", end = "")

print("\n")

#11
inStr, outStr = "파이썬###COOKBOOK$$$@@@열공중1234", ""

for i in range(0, len(inStr)) :
    if inStr[i].isalpha() == True :
        outStr += inStr[i]

print("한글/영문자만 남김 --> %s" %outStr)

#9
inStr, outStr = "Python", ""
strLen = len(inStr)

for i in range(0, strLen) :
    outStr += inStr[strLen - (i+1)]

print("내용을 거꾸로 출력 --> %s" %outStr)

