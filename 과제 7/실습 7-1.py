import random
def create_board():
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)
    board = []
    for i in range(len(seed)):
        random.shuffle(seed)
        board.append(seed)
    return board # None를 적절한 식으로 대치

print(create_board())