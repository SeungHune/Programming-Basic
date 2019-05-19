# 6. 십진수를 16진수로 변환하기

def dec2hex(dec):
    hex = ''
    while not (dec == 0):
        r = dec % 16
        if r < 10:
            hex = str(r) + hex
        elif r == 10:
            hex = 'A' + hex
        elif r == 11:
            hex = 'B' + hex
        elif r == 12:
            hex = 'C' + hex
        elif r == 13:
            hex = 'D' + hex
        elif r == 14:
            hex = 'E' + hex
        elif r == 15:
            hex = 'F' + hex
        dec = dec // 16
    return hex

print(dec2hex(52309)) # 'CC55'
print(dec2hex(2500)) # '9C4'
print(dec2hex(91)) # '5B'
print(dec2hex(256)) # '100'
print(dec2hex(2766)) # 'ACE'
print(dec2hex(3501)) # 'DAD'
print(dec2hex(3855)) # 'F0F'
print(dec2hex(4132)) # '1024'
