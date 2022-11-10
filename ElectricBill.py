print(f"""
Sunway International Business School
        Maitidevi, Kathmandu
*................*...................*
""")
name = input("Enter your name: ")
address = input("Enter your address:")
bill = int(input("Enter your unit: "))
if bill <= 100:
    rate = bill * 0
    dis = 0
elif 101 <= bill <= 200:
    rate = ((bill - 100) * 5)
    dis = 0
elif 201 <= bill <= 500:
    rate = 500 + ((bill - 200) * 10)
    dis = 0
elif bill >= 501:
    rate = ((500 + (bill-200) * 10))
    dis = ((bill-500) * 10 * 10)/100 # 100
else:
    print("Thank You")
print(f"""
Sunway International Business School
        Maitidevi, Kathmandu
*................*...................*
""")
print("Bill Per Unit:",rate)
print(f"""Customer Name: {name}
Customer Address: {address}
Consumed unit: {bill}
Total amount to be paid:Rs.{rate}
Total discount price:Rs.{dis}
Total amount after discount:Rs.{rate-dis}
{name} Customer of Sunway International Electricity Billing System 
has to pay total amount Rs.{rate-dis} and got discount of Rs.{dis}""")