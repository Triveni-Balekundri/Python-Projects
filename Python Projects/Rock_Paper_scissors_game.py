import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# user choice
types_list=[rock,paper,scissors]
type=int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print("\nYou choose: ")
if type>=0 and type<=2:
    print(types_list[type])

# computer choice
print("\n Computer chose: ")
random_type=random.randint(0,2)
print(types_list[random_type])

# if rock and paper then i lose
if type==0 and random_type==1:
    print("\nYou Lose")
#     if paper and rock then I won
elif type==1 and random_type==0:
    print("\nYou won !")
#     if rock and scissor then I won
elif type==0 and random_type==2:
    print("\n you Won !")
# if scissor and paper I won
elif type==2 and random_type==1:
    print("I won")
elif type==2 and random_type==0:
    print("I lose")
else:
    print("invalid Choice. You Lose ! ")



# please, complete any missing if elif conditions.


