import random
from cardgame import *

#멤버 불러오기
def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

#정보 쓰기
def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + str(tries) + ',' + str(wins) + "," + str(chips) + '\n'
        file.write(line)
    file.close()

#로그인 하기
def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if (username in members):
        if (members.get(username)[0] == trypasswd):
            tries = members.get(username)[1]
            wins = members.get(username)[2]
            chips = members.get(username)[3]
            #판수와 이긴횟수 보여주기
            print("You played",tries,"games and won",wins,"of them.")
            #승률 보여주기
            if(int(tries) > 0):
                win_rate = round(float(wins)/int(tries)*100, 1)
            else:
                win_rate = 0.0
            print("Your all-time winning percentage is",win_rate,"%")
            #칩수 보여주기
            if(int(chips) >= 0):
                print("You have",chips,"chips.")
            else:
                print("You owe", abs(chips),"chips.")
            return username, tries, wins, chips, members, trypasswd
        else:
            return login(members)
    else:
        members[username] = (trypasswd, 0, 0, 0)
        store_members(members)
        return username, 0, 0.0, 0, members, trypasswd

#상위 5명 보여주기
def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(),key=lambda x: x[1][3],reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    a = 0
    for i in sorted_members[:5]:
        if((i[1])[3] > 0):
            a = a + 1
            print(str(a)+".",i[0],":",(i[1])[3])

def black_jack():
    members = load_members()
    print("Welcome to SMaSH Casino!")
    username, tries, wins, chips, members, passwd = login(members)
    while True:
        print("--------------------")
        deck = fresh_deck()
        dealer = []
        player = []
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)

        print("My cards are : ")
        print(" ", "****","**")
        print(" ",dealer[1]["suit"],dealer[1]["rank"])

        show_cards(player, "Your cards are : ")

        score_player = count_score(player)
        score_dealer = count_score(dealer)

        while(score_player < 21):
            if (more("Hit? (y/n) : ") == True):
                card, deck = hit(deck)
                print(" ",card["suit"],card["rank"])
                player.append(card)
                score_player = count_score(player)
            else:
                break

        while (score_dealer <= 16):
            card, deck = hit(deck)
            dealer.append(card)
            score_dealer = count_score(dealer)

        if (score_player == 21):
            print("Blackjack! You won.")
            chips = chips + 2
            tries = tries + 1
            wins = wins + 1
        elif (score_dealer > score_player):
            if(score_dealer > 21 and score_player < 21):
                show_cards(dealer, "My cards are : ")
                print("I bust! You won.")
                chips = chips + 1
                tries = tries + 1
                wins = wins + 1
            else:
                show_cards(dealer, "My cards are : ")
                print("I won.")
                chips = chips - 1
                tries = tries + 1
        elif(score_dealer < score_player):
            if (score_player > 21):
                print("You bust! I won.")
                chips = chips - 1
                tries = tries + 1
            else:
                show_cards(dealer, "My cards are : ")
                print("You won.")
                chips = chips + 1
                tries = tries + 1
                wins = wins + 1
        else:
            if (score_player > 21):
                print("You bust! I won.")
                chips = chips - 1
                tries = tries + 1
            else:
                show_cards(dealer, "My cards are : ")
                print("We draw.")
                tries = tries + 1
                wins = wins + 0.5


        print("Chips : ",chips)

        if (more("Play more? (y/n) : ") == True):
            continue
        else:
            members[username] = (passwd, tries, wins, chips)
            store_members(members)
            print("-----")
            print("You played", tries, "games and won", wins, "of them.")
            if (int(tries) > 0):
                win_rate = round(float(wins) / int(tries) * 100, 1)
            else:
                win_rate = 0.0
            print("Your all-time winning percentage is", win_rate, "%")
            show_top5(load_members())
            print("-----")
            print("Bye!")
            break

black_jack()