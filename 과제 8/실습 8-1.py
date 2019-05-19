import random

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

fresh_deck()