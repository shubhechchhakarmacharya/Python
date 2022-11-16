from datetime import date
print(f"""
-------------------------------------
Sunway Int'l College Grading System
        Maitidevi, Kathmandu
*................*...................*
                                Date:{date.today()}
""")
name = input("Enter your name: ")
faculty = input("Enter your faculty: ")
intake = input("Enter your intake date: ")
address = input("Enter your address: ")
program = input("Enter your program: ")
Applied, Entrepreneurship, Mobile, DSA, Communication = input("Enter Marks for Applied Programing, "
                                                              "Basic Entrepreneurship, "
                                                              "Mobile Programing, "
                                                              "Data Structure and Algorithm,"
                                                              "Communication").split(",")
Applied = int(Applied)
Entrepreneurship = int(Entrepreneurship)
Mobile = int(Mobile)
DSA = int(DSA)
Communication = int(Communication)
percentage = ((Applied + Entrepreneurship + Mobile + DSA + Communication) / 5)
print(f"""
--------------------------------------------------------------------------------
Sunway Int'l College Grading System
        Maitidevi, Kathmandu
*................*...................*
""")
print(f"""Student Name: {name}
Student Faculty: {faculty}
Student Intake: {intake}
Student Address: {address}
Student Program: {program}
Student Percentage: {percentage}
-----------------------******------------------------**********-------------------
""")
if percentage >= 90:
    print(f"Student {name} is awarded by Grade A+.")
elif 90 > percentage >= 80:
    print(f"Student {name} is awarded by Grade A.")
elif 80 > percentage >= 70:
    print(f"Student {name} is awarded by Grade B+.")
elif 70 > percentage >= 60:
    print(f"Student {name} is awarded by Grade B-.")
elif 60 > percentage >= 50:
    print(f"Student {name} is awarded by Grade B.")
elif 50 > percentage >= 40:
    print(f"Student {name} is awarded by Grade C+.")
elif 40 > percentage >= 30:
    print(f"Student {name} is awarded by Grade D.")
elif percentage < 30:
    print(f"Student {name} is awarded by Grade F.")
else:
    print("Thank you")

