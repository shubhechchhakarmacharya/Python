

def takeInformation():
    inputString = input("Enter any character to check : ")
    return inputString


def checkInput(inputString):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(0, len(inputString)):
        if ('A' <= inputString[i] <= 'Z'):
            a += 1
        elif ('a' <= inputString[i] <= 'z'):
            b += 1
        elif ('0' <= inputString[i] <= '9'):
            c += 1
        else:
            d += 1
    return a, b, d, c


def displayOutput(inputString, upperCase, lowerCase, specialCharacter, numericData):
    print(f"""
        WELCOME TO SUNWAY CHARACTER CHECK SYSTEM
                MAITIDEVI, KATHMANDU

    String '{inputString}' has :
    Number of UpperCase           = {upperCase}
    Number of LowerCase           = {lowerCase}
    Number of Special Character   = {specialCharacter}
    Number of Numeric Data        = {numericData}

    \t\t Thank you for the visit
    """)


inputString = takeInformation()
upperCase, lowerCase, specialCharacter, numericData = checkInput(inputString)
print()
print("Output of System")
displayOutput(inputString, upperCase, lowerCase, specialCharacter, numericData)