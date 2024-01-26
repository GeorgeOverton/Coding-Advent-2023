def backpackDupes():
    file = open('backpack.txt')
    total = 0
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ,"A", "B", "C", "D",
                  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                  "T", "U", "V", "W", "X", "Y", "Z"]
    for line in file:
        dups = []
        lists = Convert(line)
        middle_index = len(lists)//2
        first_half = lists[:middle_index]
        second_half = lists[middle_index:]
        for i in second_half:
            for j in first_half:
                if i == j:
                    if i in dups:
                        break
                    else:
                        dups.append(i)
        for z in dups:
            value = characters.index(z)
            total += value + 1
        print(total)
    print(total)
    file.close()
    
def teamBadge():
    file = open('backpack.txt')
    total = 0
    teams = []
    lister = []
    found = False
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ,"A", "B", "C", "D",
                  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                  "T", "U", "V", "W", "X", "Y", "Z"]
    for line in file:
        dups = []
        lists = Convert(line)
        lister.append(lists)
    print(len(lister))
    for i in range(0,len(lister)-0,3):
        lister[i]
        print(lister[i][0] + lister[i+1][0] + lister[i+2][0])
        found = False
        for p in lister[i]:
            for j in lister[i+1]:
                if p == j:
                    for q in lister[i+2]:
                        if p == q and p != "\n":
                            teams.append(p)
                            found = True
                            break
                if found == True:
                    break
            if found == True:
                break
    print(len(teams))
    for z in teams:
        value = characters.index(z)
        total += value + 1
    print(total)
    file.close()
    

def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

teamBadge()
