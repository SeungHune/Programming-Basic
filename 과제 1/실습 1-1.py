y = int(input("""
해와 달 수를 날짜 수로 환산해 드립니다.
몇 년? """))

m = int(input("몇 개월? "))

days = y*365 + m*30

print(y, "년" ,m, "개월은 날짜로 환산하면" ,days, "일입니다.")
