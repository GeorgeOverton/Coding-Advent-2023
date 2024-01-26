def contains():
    file = open('jobs.txt')
    number = 0
    for line in file:
        lists = line.split(",")
        first_half = lists[0]
        first_half = first_half.split("-")
        second_half = lists[1]
        second_half = second_half.split("-")
        if int(first_half[0]) <= int(second_half[0]) and int(first_half[1]) >= int(second_half[1]):
            number += 1
        elif int(first_half[0]) >= int(second_half[0]) and int(first_half[1]) <= int(second_half[1]):
            number += 1
    print(number)
    file.close()


def containsOverlap():
    file = open('jobs.txt')
    number = 0
    for line in file:
        lists = line.split(",")
        first_half = lists[0]
        first_half = first_half.split("-")
        second_half = lists[1]
        second_half = second_half.split("-")
        if int(first_half[0]) <= int(second_half[0]) and int(first_half[1]) >= int(second_half[0]):
            number += 1
        elif int(first_half[0]) >= int(second_half[0]) and int(first_half[0]) <= int(second_half[1]):
            number += 1
    print(number)
    file.close()

    

contains()
        
        
