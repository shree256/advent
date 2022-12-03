def day1():
    f = open("day1.txt","r")
    total_calories = []
    temp = 0
    
    while True:
        calorie = f.readline()
        if calorie == '':
            total_calories.append(temp)
            break
        if calorie == "\n":
            total_calories.append(temp)
            temp = 0
        else:
            temp += int(calorie.strip())

    total_calories.sort(reverse=True)

    print("part1: "+str(max(total_calories)))
    print("part2: "+str(sum(total_calories[0:3])))

day1()