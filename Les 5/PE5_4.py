from time import *


def write(path, string):
    with open(path, 'a')as file:
        file.write(string)

while True:
    write("hardlopers.txt", str(strftime("%a %d %b %Y, %X")) + " " + input("Geef uw naam op: ") + "\r")
