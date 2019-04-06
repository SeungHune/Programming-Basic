#기수정렬
def radixsort(ds,length):
    if (ds == []):
        return []
    else :
        n = 0
        for k in range(length, 0, -1):
            to0 = []
            to1 = []
            to2 = []
            to3 = []
            to4 = []
            to5 = []
            to6 = []
            to7 = []
            to8 = []
            to9 = []
            for i in ds:
                if (i[k-1] == "0"):
                    to0.append(i)
                if (i[k-1] == "1"):
                    to1.append(i)
                if (i[k-1] == "2"):
                    to2.append(i)
                if (i[k-1] == "3"):
                    to3.append(i)
                if (i[k-1] == "4"):
                    to4.append(i)
                if (i[k-1] == "5"):
                    to5.append(i)
                if (i[k-1] == "6"):
                    to6.append(i)
                if (i[k-1] == "7"):
                    to7.append(i)
                if (i[k-1] == "8"):
                    to8.append(i)
                if (i[k-1] == "9"):
                    to9.append(i)
                ds = to0 + to1 + to2 + to3 + to4 + to5 + to6 + to7 + to8 + to9
    return ds

print(radixsort([],3))
#=> []
print(radixsort(["239"],3))
#=> ['239']
print(radixsort(["170",'045','075','090','002','024','802','066'],3))
#=> ['002', '024', '045', '066', '075', '090', '170', '802']
print(radixsort(["239",'234','879','878','123','358','416','317','137','225'],3))
#=> ['123', '137', '225', '234', '239', '317', '358', '416', '878', '879']
print(radixsort(["0508", "0515", "1225", "0915", "1111", "0101", "0318", "0301", "0815"],4))
#=> ['0101', '0301', '0318', '0508', '0515', '0815', '0915', '1111', '1225']