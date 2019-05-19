import random

# deck 만들기
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    # 중첩 for 문으로 52장의 카드를 만들어 리스트 deck을 만든다.
    for a in suits:
        for b in ranks:
            deck.append({"suit" : a , "rank" : b})
    # deck을 무작위로 섞는다.
    random.shuffle(deck)
    return deck

# 카드 뽑기
def hit(deck):
    if (len(deck) == 0): # deck이 비어있으면:
        # 카드 1벌을 새로 만듬
        deck = fresh_deck()
    return (deck[0], deck[1:])   # (맨 앞의 카드 한장 , 남은 deck)

# 점수 계산
def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        print(card)
        # card의 값을 평가하여 score에 더함 (A는 11로 계산)
        if (card["rank"] == 2):
            score = score + 2
        elif (card["rank"] == 3):
            score = score + 3
        elif (card["rank"] == 4):
            score = score + 4
        elif (card["rank"] == 5):
            score = score + 5
        elif (card["rank"] == 6):
            score = score + 6
        elif (card["rank"] == 7):
            score = score + 7
        elif (card["rank"] == 8):
            score = score + 8
        elif (card["rank"] == 9):
            score = score + 9
        elif (card["rank"] == 10):
            score = score + 10
        elif (card["rank"] == "A"):
            number_of_ace = number_of_ace + 1
            score = score + 11
        else:
            score = score + 10
    # score가 21이 넘고 A가 있으면 score를 재조정함
    if (score > 21 and number_of_ace > 0):
        score = score - 10
        number_of_ace = number_of_ace -1
        if (score > 21 and number_of_ace > 0):
            score = score - 10
            number_of_ace = number_of_ace - 1
            if (score > 21 and number_of_ace > 0):
                score = score - 10
                number_of_ace = number_of_ace - 1
                if (score > 21 and number_of_ace > 0):
                    score = score - 10
                    number_of_ace = number_of_ace - 1
    # A가 2장 이상 있을 수 있음에 유의
    return score

# 더 할지 물어보기
def more(message):
    answer = input(message)
    while not (answer == "n" or answer == "y"):
        answer = input(message)
        continue
    if (answer == "y"):
        return True
    elif(answer == "n"):
        return False

# 카드 보여주기
def show_cards(cards,message):
    print(message)
    for card in cards:
        # card를 보기 좋게 한줄에 프린트
        print(card ,"\n")

def black_jack():
