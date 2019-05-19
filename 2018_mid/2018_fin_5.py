def hex2dec(hex):
    hex = hex[::-1]
    length = len(hex)
    dec = 0
    for i in range(length):
        h = hex[i]
        if (h=="A"):
            h = 10
        if (h == "B"):
            h = 11
        if (h=="C"):
            h = 12
        if (h == "D"):
            h = 13
        if (h == "E"):
            h = 14
        if (h == "F"):
            h = 15
        temp = int(h)
        dec = dec + (temp * 16**i)
    return dec

print(hex2dec("9C4")) # 2500
print(hex2dec('5B')) # 91
print(hex2dec('100')) # 256
print(hex2dec('ACE')) # 2766
print(hex2dec('DAD')) # 3501
print(hex2dec('F0F')) # 3855
print(hex2dec('1024')) # 4132
print(hex2dec('CC55')) # 52309