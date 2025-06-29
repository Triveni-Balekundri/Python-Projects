import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Here we have used all the basic concepts of I/O
# random module and functions | for() | range() | list and its functions
# And how to use a string variable

password_list=[]

# Easy version-Generate the password in sequence. Letters, then symbols, then numbers.
# df!@12 - pattern for generating a password

password=""

for l in range(0,nr_letters):
    random_letter=random.choice(letters)
    password=password+random_letter
    # print(random_letter)
for s in range(1,nr_symbols+1):
    random_sym = random.choice(symbols)
    password = password + random_sym

for n in range(1,nr_numbers+1):
    random_num = random.choice(numbers)
    password = password + random_num
    # print(random_num)

print("Your (Easy version) Generated Password: ",password)


# Hard Version of Generating a shuffled password using a list:

# So the example above might look like this: x$d24g*f9
# every time you generate a password,
# the positions of the symbols, numbers, and letters are different.

passw=""
for l in range(0,nr_letters):
    random_letter=random.choice(letters)
    password_list.append(random_letter)

for s in range(1,nr_symbols+1):
    random_sym = random.choice(symbols)
    password_list.append(random_sym)

for n in range(1,nr_numbers+1):
    random_num = random.choice(numbers)
    password_list.append(random_num)

# By this we can shuffle the elements present in a list.
random.shuffle(password_list)

# Here we are printing with the help of a for loop in the form of string using a variable 'passw'
for char in password_list:
    passw+=char;
print("Your (hard version) Generated Password: ",passw)
