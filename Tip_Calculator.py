print("Welcome to the tip calculator")
bill = float(input("What is the total bill : "))
tip = int(input("What percentage tip wou;d you like to give? 10, 12, 15 : "))
people = int(input("How many people split the bill : "))
tips_as_percentage = tip/100
total_tip_ammount = bill *tips_as_percentage
total_bill = bill+total_tip_ammount
per_person = total_bill / people
print(f"Your total bill is ${total_bill :.2f} \nTotal person = {people} \nEvery person contribut amount of ${per_person :.2f} \nThanks for visiting .")