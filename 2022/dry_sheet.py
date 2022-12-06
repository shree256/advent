import re


def day1():
    f = open("day1.txt", "r")
    total_calories = []
    temp = 0

    while True:
        calorie = f.readline()
        if calorie:
            if calorie == "\n":
                total_calories.append(temp)
                temp = 0
            else:
                temp += int(calorie.strip())
        else:
            total_calories.append(temp)
            break

    total_calories.sort(reverse=True)

    print("part1: " + str(max(total_calories)))
    print("part2: " + str(sum(total_calories[0:3])))


def day2_1():
    f = open("day2.txt", "r")

    strategy_score = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    draw_map = {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }

    win_map = {
        "A": "Y",
        "B": "Z",
        "C": "X",
    }

    score = 0

    while True:
        strategy = f.readline()
        if strategy:
            # Part1
            opponent, me = strategy.strip().split(" ")
            if draw_map[opponent] == me:
                score += strategy_score[me] + 3
            elif win_map[opponent] == me:
                score += strategy_score[me] + 6
            else:
                score += strategy_score[me]

            # Part2
            # col1, col2 = strategy.strip().split(" ")
            # if col2 == "Y":
            #     score += (draw_map_points[col1]+ 3)
            # elif col2 == "Z":
            #     score += (win_map_points[col1] + 6)
            # else:
            #     score += (lose_map_points[col1])

        else:
            break

    print("score: " + str(score))


def day2_2():
    f = open("day2.txt", "r")

    draw_map_points = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    win_map_points = {
        "A": 2,
        "B": 3,
        "C": 1,
    }

    lose_map_points = {
        "A": 3,
        "B": 1,
        "C": 2,
    }

    score = 0

    while True:
        strategy = f.readline()
        if strategy:
            Part2
            col1, col2 = strategy.strip().split(" ")
            if col2 == "Y":
                score += draw_map_points[col1] + 3
            elif col2 == "Z":
                score += win_map_points[col1] + 6
            else:
                score += lose_map_points[col1]
        else:
            break


def get_char_score(c):
    if ord(c) > 97:
        return ord(c) - 96
    else:
        return ord(c) - 38


def day3_1():
    f = open("day3.txt", "r")
    score = 0

    while True:
        rucksack = f.readline()
        if rucksack:
            sack_len = len(rucksack) // 2
            compartment1 = rucksack[0:sack_len]
            compartment2 = rucksack[sack_len:-1]

            for c1 in compartment1:
                if c1 in compartment2:
                    score += get_char_score(c1)
        else:
            break

    print("score: " + str(score))


def day3_2():
    f = open("day3.txt", "r")
    score = 0

    while True:
        flag = False
        group1 = f.readline()
        group2 = f.readline()
        group3 = f.readline()
        if group3:
            for c1 in group1:
                for c2 in group2:
                    if c2 == c1:
                        for c3 in group3:
                            if c3 == c1:
                                score += get_char_score(c3)
                                flag = True
                                break
                    if flag:
                        break
                if flag:
                    break
        elif group1:
            for c1 in group1:
                for c2 in group2:
                    if c2 == c1:
                        score += get_char_score(c2)
                        flag = True
                        break
                if flag:
                    break
        else:
            break
    print("score: " + str(score))


def day5():
    f = open("day5.txt", "r")

    cargo = [
        ["G", "F", "V", "H", "P", "S"],
        ["G", "J", "F", "B", "V", "D", "Z", "M"],
        ["G", "M", "L", "J", "N"],
        ["N", "G", "Z", "V", "D", "W", "P"],
        ["V", "R", "C", "B"],
        ["V", "R", "S", "M", "P", "W", "L", "Z"],
        ["T", "H", "P"],
        ["Q", "R", "S", "N", "C", "H", "Z", "V"],
        ["F", "L", "G", "P", "V", "Q", "J"],
    ]

    while True:
        operation = re.split(r"move | from | to ", f.readline().strip())

        if operation and len(operation) > 1:
            crates, stack_from, stack_to = (
                int(operation[1]),
                int(operation[2]) - 1,
                int(operation[3]) - 1,
            )

            stack1 = cargo[stack_from]
            stack2 = cargo[stack_to]

            # Part1
            for _ in range(crates):
                stack2.append(stack1.pop())

            # Part 2
            # temp = []
            # for _ in range(crates):
            #     temp.append(stack1.pop())
            # temp.reverse()
            # stack2 += temp

            cargo[stack_from] = stack1
            cargo[stack_to] = stack2

        else:
            break

    for stack in cargo:
        print(stack[-1], end="")

def day6(marker_length=4):
    f = open("day6.txt", "r")
    message = f.readline()
    marker_found = False
    i = 0
    while True:
        marker = message[i:i+marker_length]
        j=0
        while True:
            if j<marker_length:
                if marker[j+1:].find(marker[j])<0:
                    j+=1
                else:
                    i+=1
                    break
            else:
                marker_found = True 
                break
        if marker_found:
            print("Marker index: "+str(i+marker_length))
            print("Marker: "+marker)
            break