#13
import turtle
import random
import math
from tkinter.simpledialog import*

inStr = ""
swidth, sheight = 500, 500
txtSize = 20
distance = 200

turtle.title("거북이로 문장쓰기")
turtle.shape("turtle")
turtle.setup(width = swidth, height = sheight)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = input("문장을 입력하시오 : ")

for i in range(len(inStr)) :
    angle = 360*2/len(inStr)
    radian = 3.14 * angle/180 * i
    distance -= 200/len(inStr)
    tX = distance*math.cos(radian);tY = distance*math.sin(radian)
    r = random.random() ; g = random.random() ; b = random.random()

    turtle.goto(tX,tY)
    turtle.pencolor((r, g, b))
    turtle.write(inStr[i], font = ("맑은 고딕", 20, "bold"))

turtle.done()
