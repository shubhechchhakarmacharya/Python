# Read the data from file "data.txt" and check the line starting from "u" character.
def readfile():
    f = open("C:/Users/shubh/PycharmProjects/Python/data.txt", "r")
    for i in f:

        if i[0] == "u":
            print("Yes")
        else:
            print("No")


readfile()
