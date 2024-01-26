class Knot:

    def __init__(self, head):
        self.position = [0,0]
        self.head = head

    def move(self):
        headpos = self.head.getPosition()
        difference = [0,0]
        difference[0] = headpos[0] - self.position[0]
        difference[1] = headpos[1] - self.position[1]
        if difference[1] >= 1 and difference[0] > 1 or difference[1] > 1 and difference[0] >= 1:
            self.position[1] += 1
            self.position[0] += 1
        elif difference[1] >= 1 and difference[0] < -1 or difference[1] > 1 and difference[0] <= -1:
            self.position[1] += 1
            self.position[0] += -1
        elif difference[0] >= 1 and difference[1] < -1 or difference[0] > 1 and difference[1] <= -1:
            self.position[1] += -1
            self.position[0] += 1
        elif difference[0] <= -1 and difference[1] < -1 or difference[0] < -1 and difference[1] <= -1:
            self.position[1] += -1
            self.position[0] += -1
        elif difference[0] > 1:
            self.position[0] += 1
        elif difference[1] > 1:
            self.position[1] += 1
        elif difference[0] < -1:
            self.position[0] += -1
        elif difference[1] < -1:
            self.position[1] += -1
        return self.position

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position



def bridgeknots():
    file = open('knotmoves.txt')
    headvect = [0,0]
    tailvect = [0,0]
    difference = [0,0]
    visited = []
    num = 1
    for line in file:
        lines = line.split()
        direction = lines[0]
        steps = lines[1]
        for i in range(int(steps)):
            if direction == "U":
                headvect[1] += 1
                difference[1] += 1
            elif direction == "D":
                headvect[1] += -1
                difference[1] += -1
            elif direction == "R":
                headvect[0] += 1
                difference[0] += 1
            elif direction == "L":
                headvect[0] += -1
                difference[0] += -1
            if difference[1] >= 1 and difference[0] > 1 or difference[1] > 1 and difference[0] >= 1:
                tailvect[1] += 1
                tailvect[0] += 1
                difference[1] += -1
                difference[0] += -1
            elif difference[1] >= 1 and difference[0] < -1 or difference[1] > 1 and difference[0] <= -1:
                tailvect[1] += 1
                tailvect[0] += -1
                difference[1] += -1
                difference[0] += 1
            elif difference[0] >= 1 and difference[1] < -1 or difference[0] > 1 and difference[1] <= -1:
                tailvect[1] += -1
                tailvect[0] += 1
                difference[1] += 1
                difference[0] += -1
            elif difference[0] <= -1 and difference[1] < -1 or difference[0] < -1 and difference[1] <= -1:
                tailvect[1] += -1
                tailvect[0] += -1
                difference[1] += 1
                difference[0] += 1
            elif difference[0] > 1:
                tailvect[0] += 1
                difference[0] += -1
            elif difference[1] > 1:
                tailvect[1] += 1
                difference[1] += -1
            elif difference[0] < -1:
                tailvect[0] += -1
                difference[0] += 1
            elif difference[1] < -1:
                tailvect[1] += -1
                difference[1] += 1
            if tailvect not in visited:
                temp = [0,0]
                temp[0] = tailvect[0]
                temp[1] = tailvect[1]
                visited.append(temp)
    print(len(visited))


def rope():
    file = open('knotmoves.txt')
    head = Knot("null")
    knots = []
    visited = []
    prevknot = head
    for j in range(9):
        knot = Knot(prevknot)
        knots.append(knot)
        prevknot = knot
    print(head)
    print(knots)
    for line in file:
        lines = line.split()
        direction = lines[0]
        steps = lines[1]
        for i in range(int(steps)):
            if direction == "U":
                head.setPosition([head.getPosition()[0] , head.getPosition()[1] + 1])
            elif direction == "D":
                head.setPosition([head.getPosition()[0] , head.getPosition()[1] - 1])
            elif direction == "R":
                head.setPosition([head.getPosition()[0] + 1 , head.getPosition()[1]])
            elif direction == "L":
                head.setPosition([head.getPosition()[0] - 1 , head.getPosition()[1]])
            for z in knots:
                z.move()
                if z.getPosition() not in visited:
                    temp = [0,0]
                    temp[0] = z.getPosition()[0]
                    temp[1] = z.getPosition()[1]
                    visited.append(temp)
    print(visited)

rope()
                
            
