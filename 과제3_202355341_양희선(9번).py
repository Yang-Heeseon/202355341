# 9번
hap, i = 0, 0

for i in range (3333,10000) :
    if i % 1234 != 0 :
        continue

    hap += i

    if hap + i >= 100000 :
        break

print("3333~9999 중 1234의 배수의 합계 : %d" %hap)

# 3333~9999 중 1234의 배수 구하기
i = 0
for i in range (3333,10000) :
    if i % 1234 == 0 :
        print(i)
# => 3702, 4936, 6170, 7404, 8638, 9872


# 9번* (1234의 배수가 아닌 수의 합계)
hap, i = 0, 0

for i in range (3333,10000) :
    if i % 1234 == 0 :
        continue

    hap += i

    if hap + i >= 100000 :
        break

print("3333~9999 중 1234의 배수가 아닌 수의 합계 : %d" %hap)
