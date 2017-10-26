def getFileData(path):
    with open(path , 'r')as file:
        for line in file:
            data = line.split(', ')
            print("{1} heeft kaartnummer {0}".format(data[0], data[1].strip()))

getFileData('Kaartnummers.txt')
