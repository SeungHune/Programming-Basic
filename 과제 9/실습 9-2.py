def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(),key=lambda x: x[1][3],reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    a = 0
    for i in sorted_members[:5]:
        if((i[1])[3] > 0):
            a = a + 1
            print(str(a)+".",i[0],":",(i[1])[3])
    # sorted_members[:5]의 원소를 차례대로 참고하여 보여주되 0이하는 무시한다.



members = {"doh": ("sid73", 993, 550, 35),
 "didi": ("edd484", 130, 55, 10),
 "hy": ("er878re", 35, 18, 2),
 "dr": ("qwert", 18, 8, 0),
 "who": ("poiuy", 34, 18, 0)}

show_top5(members)