big = int(input("""
동전 합산 해줄께... 음수는 넣지마.
오백원짜리 몇개? """))
middle = int(input("백원짜리 몇개? "))
small = int(input("오십원짜리 몇개? "))
ssmall = int(input("십원짜리 몇개? "))
total = big*500 + middle*100 + small*50 + ssmall*10
print("자기가 갖고 있는 동전은 총" ,total, "원 이야.")
