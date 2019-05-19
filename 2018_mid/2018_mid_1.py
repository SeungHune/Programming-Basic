def complement9(n):  # 자연수라고 가정
    s = str(n)
    ans = ""
    for c in s:
    # pass # 이 부분을 채우자
        a = abs(int(c) - 9)
        ans = ans + str(a)
    return int(ans)

print(complement9(0))
print(complement9(9))
print(complement9(4))
print(complement9(18))
print(complement9(40))
print(complement9(307))
print(complement9(9999))
print(complement9(9142))
print(complement9(9965))
