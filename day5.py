def containsOverlap():
    file = open('containers.txt')
    stack = [["R","S","L","F","Q"],
             ["N","Z","Q","G","P","T"],
             ["S","M","Q","B"],
             ["T","G","Z","J","H","C","B","Q"],
             ["P","H","M","B","N","F","S"],
             ["P","C","Q","N","S","L","V","G"],
             ["W","C","F"],
             ["Q","H","G","Z","W","V","P","M"],
             ["G","Z","D","L","C","N","R"]]

    movesreached = False
    for line in file:
        liny = line.strip()
        if liny == "":
            movesreached = True
        elif movesreached == True:
            splitedline = line.split()
            splitedline.remove("move")
            splitedline.remove("from")
            splitedline.remove("to")
            numbermoved = int(splitedline[0])
            movedfrom = stack[int(splitedline[1])-1]
            movedto = stack[int(splitedline[2])-1]
            size = len(stack[int(splitedline[1])-1])
            loop = True
            num = 0
            while loop == True:
                removed = movedfrom.pop(len(movedfrom)-1)
                movedto.append(removed)
                num += 1
                if num == numbermoved:
                    loop = False
    print(stack)
    final = ""
    for i in stack:
        final += i[len(i)-1]
    print(final)

def containsOverlap2():
    file = open('containers.txt')
    stack = [["R","S","L","F","Q"],
             ["N","Z","Q","G","P","T"],
             ["S","M","Q","B"],
             ["T","G","Z","J","H","C","B","Q"],
             ["P","H","M","B","N","F","S"],
             ["P","C","Q","N","S","L","V","G"],
             ["W","C","F"],
             ["Q","H","G","Z","W","V","P","M"],
             ["G","Z","D","L","C","N","R"]]

    movesreached = False
    for line in file:
        liny = line.strip()
        if liny == "":
            movesreached = True
        elif movesreached == True:
            splitedline = line.split()
            splitedline.remove("move")
            splitedline.remove("from")
            splitedline.remove("to")
            numbermoved = int(splitedline[0])
            movedfrom = stack[int(splitedline[1])-1]
            movedto = stack[int(splitedline[2])-1]
            size = len(stack[int(splitedline[1])-1])
            temp = []
            loop = True
            num = 0
            while loop == True:
                removed = movedfrom.pop(len(movedfrom)-1)
                temp.append(removed)
                num += 1
                if num == numbermoved:
                    loop = False

            temp.reverse()       
            for nuber in temp:
                movedto.append(nuber)
    print(stack)
    final = ""
    for i in stack:
        final += i[len(i)-1]
    print(final)

        



containsOverlap2()
