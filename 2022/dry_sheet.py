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


def day2():
    f = open("day2.txt", "r")

    # Part1
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

    # Part2
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


day2()
