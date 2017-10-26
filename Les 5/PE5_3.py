def getFileData(path):
    with open(path, 'r') as file:
        lines = 0
        highest = 0
        highestLine = 0

        for line in file:
            lines += 1
            data = line.split(', ')
            if (int(data[0]) > highest):
                highest = int(data[0])
                highestLine = lines

        print("Deze file telt {} regels".format(lines))
        print("Het grootste kaartnummer is: {} dit nummer staat op regel {}".format(highest, highestLine))


getFileData('kaartnummers.txt')
