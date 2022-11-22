number = int(input("Enter random number: "))
print("The pattern formed is:")
for i in range(number):
    for j in range(i):
        print("* ", end=" ")
    print()
for i in range(number):
    for j in range(number-i):
        print("* ", end=" ")
    print()