
### 11. 아나그램 확인 (sort() 함수 사용 금지)

def isanagram(word1, word2):
    while word1 != '':
        if word1[0] in word2:
            if(len(word1) != len(word2)):
                return False
            for i in word1:
                if(word1.find(i) == word2.find(i)):
                    return True
            return False
        else:
            return False
    return word2 == ''



print(isanagram('', ''))  # True
print(isanagram('z', 'z'))  # True
print(isanagram('zz', 'z'))  # False
print(isanagram('z', 'zz'))  # False
print(isanagram('silent', 'listen'))  # True
print(isanagram('silent', 'listens'))  # False
print(isanagram('elvis', 'lives'))  # True
print(isanagram('restful', 'fluster'))  # True
print(isanagram('restfully', 'fluster'))  # False
print(isanagram('문전박대', '대박전문'))  # True