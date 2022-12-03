def day1():
    f = open("day1.txt","r")
    arr = []
    temp = 0
    while True:
        val = f.readline()
        if val == '':
            arr.append(temp)
            break
        if val == "\n":
            arr.append(temp)
            temp = 0
        else:
            temp += int(val.strip())
    print(max(arr))

day1()