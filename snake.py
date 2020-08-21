tab = []
line = []
for i in range(40):
    for j in range(12):
        line.append("X")
    tab.append(line)
for i in range(40):
    for j in range(12):
        print(tab[i][j], end="")
    print("")
print("=snakeboard=")