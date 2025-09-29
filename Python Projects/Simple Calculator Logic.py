def add(n1, n2):
    return n1 + n2

def subt(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


choice="y"
while choice == "y":
    print("--------------------------------------------------")
    n1= float(input("Whats the First number? : "))
    opt = ""
    opt = input("Pick an Operation (+,-,/,*) : ")
    n2= float(input("Whats the Second number? : "))
    if opt == "+":
        print("Your Answer is: ",add(n1, n2))
    elif opt=="-":
        print("Your Answer is: ",subt(n1, n2))
    elif opt == "*":
        print("Your Answer is: ",mult(n1, n2))
    elif opt == "/":
        print("Your Answer is: ",div(n1, n2))
    choice = input("You want to continue? (y/n) : ")



