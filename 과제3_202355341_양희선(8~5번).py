#8번
hap = 0
for n in range(1234,4567) :
    if n%444 == 0 :
        hap += n

print(hap)

#  ->답 : 33300
# whlie문으로 변경

hap = 0
n = 1234

while n < 4568 :
    if n % 444 == 0 :
        hap += n
    n += 1
print(hap)


#14번
myData = [ [n*m for n in range(1,3) ] for m in range(2,4)]
print(myData)

#14번 답 : [[2, 4], [3, 6]]

#5번

nn = [100, 200, 300, 400, 500]

#5-1
print(nn[4])

#5-2
print(nn[-1])

#5-3
print(nn[-2])

#5-4
print(nn[1:4])

#5-5
print(nn[0:1])

#5-6
print(nn[2:-1])

#5-7
print(nn[0::2])

#5-8
print(nn[::-1])

#5-9
print(nn[::-2])

#5-1 답 500
#5-2 답 500
#5-3 답 400
#5-4 답 [200, 300, 400]
#5-5 답 [100]
#5-6 답 [300, 400]
#5-7 답 [100, 300, 500]
#5-8 답 [500, 400, 300, 200, 100]
#5-9 답 [500, 300, 100]
