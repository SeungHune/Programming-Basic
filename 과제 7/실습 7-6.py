def get_integer(message,i,j):
    number = input(message)
    while not (int(number) >= i and int(number) <=j): # 괄호 안에 조건식을 채운다.
        number = input(message)
    return int(number)

print(get_integer("가로줄번호(1~4): ",1,4))
print(get_integer("세로줄번호(1~4): ",1,4))