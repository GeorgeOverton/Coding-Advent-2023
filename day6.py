def packetHeader():
    file = open('packet.txt')
    filestring = file.read()
    lists = Convert(filestring)
    for i in range(0,len(lists)-3,1):
        if lists[i] != lists[i+1] and lists[i] != lists[i+2] and lists[i] != lists[i+3] and lists[i+1] != lists[i+2] and lists[i+1] != lists[i+3] and lists[i+2] != lists[i+3]:
            print(lists[i] , lists[i+1], lists[i+2], lists[i+3])
            print(i+4)
            break
    
def packetLargeHeader():
    file = open('packet.txt')
    filestring = file.read()
    lists = Convert(filestring)
    for i in range(0,len(lists)-3,1):
        testList = []
        for j in range(14):
            if lists[i+j] not in testList:
                testList.append(lists[i+j])
                if j == 13:
                    print(lists[i] , lists[i+1], lists[i+2], lists[i+3])
                    print(i+14)
            else:
                break




def Convert(string):
    list1 = []
    list1[:0] = string
    return list1



packetLargeHeader()
