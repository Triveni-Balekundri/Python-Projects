print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Another way to do this:
# bill_tip=tip/100*bill+bill
# final=bill_tip/people
# print(final)

exact_tip = (tip/100)
# print(exact_tip)

total_tip=(bill*exact_tip)
# print(total_tip)

total_bill=(bill+total_tip)
# print(total_bill)

final_amount=round(total_bill/people,2)
print("Each Person should pay: ",float(final_amount))






































