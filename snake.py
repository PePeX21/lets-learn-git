import os
tab = []
line = []
xtab = [5, 6, 7, 8]
ytab = [24, 25, 26, 27]
snake = False

for it in range (28):
    for i in range(25):
        for j in range(12):
            line.append("X")
        tab.append(line)
        line = []

    for i in range(25):
        for j in range(12):
            for s in range(4):
                if((i == ytab[s]) and (j == xtab[s])):
                    print("@", end="")
                    snake = True
            if(not snake):
                print(tab[i][j], end="")
            snake = False
        print("")

    for s in range(4):
        xtab[s] = xtab[s] - 1
        ytab[s] = ytab[s] - 1

        if(xtab[s] < 0):
            xtab[s] = 11

    print("=snakeboard=")
    os.system('CLS')