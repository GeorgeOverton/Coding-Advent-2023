def elfMaxCalories():
    elfCalories = [0]
    file = open('calories.txt')
    index = 0
    for line in file:
        if line.strip() != "":
            elfCalories[index] += int(line)
        else:
            index += 1
            elfCalories.append(0)
    total = 0
    print(max(elfCalories))
    total += max(elfCalories)
    elfCalories.remove(max(elfCalories))
    print(max(elfCalories))
    total += max(elfCalories)
    elfCalories.remove(max(elfCalories))
    total += max(elfCalories)
    print(max(elfCalories))
    elfCalories.remove(max(elfCalories))
    print(total)
    file.close()

elfMaxCalories()
