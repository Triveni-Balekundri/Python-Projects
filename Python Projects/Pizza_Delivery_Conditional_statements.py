print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# Or keep the final_bill as 0 then you add on over to it by example: final_bill+=3
# final_bill=0

if size=="S":
    # final_bill+=15
    final_bill=15
    if pepperoni=="Y":
        final_bill=final_bill+2
    if extra_cheese=="Y":
        final_bill=final_bill+1
    print(f"Your final bill is: ${final_bill}.")

elif size=="M":
    final_bill=20
    if pepperoni=="Y":
        final_bill=final_bill+3
    if extra_cheese=="Y":
        final_bill=final_bill+1
    print(f"Your final bill is: ${final_bill}.")

elif size=="L":
    final_bill=25
    if pepperoni == "Y":
        final_bill = final_bill + 3
    if extra_cheese == "Y":
        final_bill = final_bill + 1
    print(f"Your final bill is: ${final_bill}.")