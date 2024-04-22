#2번
class Car :
    color = ""
    speed = 0

    def upSpeed(self, value) :
        self.speed += value


#4번
class Horse :
    speed = 0

    def __int__(self, speed) :
        self.speed = 50


#6번
class Car :
    def method(self) :
        print("슈퍼 클래스")

class Sedan(Car) :
    def method(self) :
        print("서브 클래스")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

#6번 답 : 슈퍼 클래스 서브 클래스


#7번
class Car :
    speed = 0

    def upSpeed(self, value) :
        self.speed = self.speed + value

class RV(Car) :
    seatNum = 0

    def getSeatNum(self) :
        return self.seatNum
