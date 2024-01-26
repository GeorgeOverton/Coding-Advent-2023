import sys

class Directory:

    def __init__(self, name,previous):
        self.name = name
        self.previous = previous
        self.containsDict = []
        self.containsFiles = []

    def setPre(self , previous):
        self.previous = previous

    def getContDict(self):
        return self.containsDict

    def setContDict(self,new):
        self.containsDict.append(new)

    def setContFiles(self,new):
        self.containsFiles.append(new)
    
    def getSize(self):
        size = 0
##        print(self)
##        print(self.containsDict)
        
        for con in self.containsDict:
            size += con.getSize()
        for con in self.containsFiles:
            size += con.getSize()
        return size



class File:
    name = ""
    size = 0
    def __init__(self, size, name):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size


#############################################

def smallFiles():
    file = open('fileExplorer.txt')
    currentDir = Directory("/","null")
    directorys = []
    directorys.append(currentDir)
    biggerSize = []
    index = 0
    next(file)
    for line in file:
        lines = line.split()
        if lines[0] == "$":
            if lines[1] == "cd":
                if lines[2] == ".." and directorys[index].previous != "null":
                    index = directorys.index(directorys[index].previous)
                else:
                    for dirct in directorys[index].getContDict():
                        if dirct.name == lines[2] and type(dirct):
                            index = directorys.index(dirct)
                            break
                        elif dirct.name == lines[2] and  dirct not in directorys:
                            print("can not enter a file")
                            print(line)
            elif lines[1] == "ls":
                time = 0
        elif lines[0] == "dir":
            newDir = Directory(lines[1],directorys[index])
            directorys.append(newDir)
            directorys[index].setContDict(newDir)
        else:
            file = File(int(lines[0]), lines[1])
            directorys[index].setContFiles(file)
    for dirct in directorys:
        if dirct.getSize() <= 100000:
            biggerSize.append(dirct.getSize())
    print(biggerSize)
    print(sum(biggerSize))

def deleteingFiles():
    file = open('fileExplorer.txt')
    currentDir = Directory("/","null")
    directorys = []
    directorys.append(currentDir)
    smallSize = 0
    index = 0
    next(file)
    for line in file:
        lines = line.split()
        if lines[0] == "$":
            if lines[1] == "cd":
                if lines[2] == ".." and directorys[index].previous != "null":
                    index = directorys.index(directorys[index].previous)
                else:
                    for dirct in directorys[index].getContDict():
                        if dirct.name == lines[2] and type(dirct):
                            index = directorys.index(dirct)
                            break
                        elif dirct.name == lines[2] and  dirct not in directorys:
                            print("can not enter a file")
                            print(line)
            elif lines[1] == "ls":
                time = 0
        elif lines[0] == "dir":
            newDir = Directory(lines[1],directorys[index])
            directorys.append(newDir)
            directorys[index].setContDict(newDir)
        else:
            file = File(int(lines[0]), lines[1])
            directorys[index].setContFiles(file)
    n = 0
    smallest = 70000000
    for dirct in directorys:
        if n > 0:
            if dirct.getSize() <= smallest and dirct.getSize() >= 30000000 - (70000000 - sizeComp):
                smallSize = dirct.getSize()
                smallest = smallSize
        else:
            sizeComp = dirct.getSize()
            n += 1
    print(smallSize)


##sys.setrecursionlimit(55500)
deleteingFiles()
