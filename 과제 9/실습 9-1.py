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
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd, 0, 0, 0)
        store_members(members)
        return username, 0, 0, 0, members


# print(load_members())
mem = load_members()
print(mem.keys())
print(mem.values())
# print("doh" in mem)
# print(mem.get("doh"))
# print(mem.get("doh")[0])
# print("doh" in mem)
login(mem)


# username의 게임시도 횟수와 이긴 횟수를 members에서 가져와 보여준다.
# 예시: You played 101 games and won 54 of them.
# 승률 계산하여 %로 보여줌 (분모가 0인 오류 방지해야 함)
# 예시: Your all-time winning percentage is 53.5 %
# 칩 보유개수를 보여줌
# 예시 : 개수가 양수이면 You have 5 chips.
# 예시 : 개수가 음수이면 You owe 5 chips.