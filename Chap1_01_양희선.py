# 문제 11
#11-1
a = int('1011', 2)
print(a)

#문제 11-1 답 : 11

#11-2
a = int("1A", 16)
print(a)

#문제 11-2 답 : 26


####################

#문제 13

#문제 13 답 : 진수 표현에 맞지 않는 숫자이기 때문에 3개 다 오류

# 13-1 : 2진수는 1까지 표현 가능한데 2까지 표현하였기 때문에 오류
#13-2 : 8진수는 7까지 표현 가능한데 8까지 표현하였기 때문에 오류
#13-3 : 16진수는 F까지 표현 가능한데 G까지 표현하였기 때문에 오류

####################

#문제 15
num = 12345678
hex_num = hex(num)
oct_num = oct(num)
bin_num = bin(num)

print("10진수 ==> ", num)
print("16진수 ==> ", hex_num)
print("8진수 ==> ", oct_num)
print("2진수 ==> ", bin_num)
