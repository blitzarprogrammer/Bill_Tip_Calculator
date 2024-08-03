print("WELCOME TO THE BILL TIP CALCULATOR!")
print("What was the total bill?")
total_bill = input()
print("How much tip would you like to give? 100,200 or 500?")
tip = input()
print("How many people to split the bill?")
split = input()
convert_bill = int(total_bill)
convert_tip = int(tip)
convert_split = int(split)
Pay1 = convert_bill + convert_tip
convert_pay = int(Pay1)
Pay2 = convert_pay/convert_split
print(f"Each person should pay: {Pay2}")