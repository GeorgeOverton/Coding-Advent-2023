def grpsstrength():
    reqlist = [20, 60, 100, 140, 180, 220]
    file = open('gpscommands.txt')
    cycle = 0
    strength = 1
    total = 0
    for line in file:
        cycledet = line.split()
        cycle += 1
        if reqlist[0] == cycle:
            total += (strength*cycle)
            reqlist.remove(reqlist[0])
            print(cycle)
            print(strength)
        if len(reqlist) == 0:
            break
        if cycledet[0] == "addx":
            strength += int(cycledet[1])
            cycle += 1
            if reqlist[0] == cycle:
                total += (strength*cycle)
                reqlist.remove(reqlist[0])
                print(cycle)
                print(strength)
                if len(reqlist) == 0:
                    break
    print(total)


grpsstrength()   
