import random

# random_integer=random.randint(1,100 )
# print(random_integer)

# random_float=random.random()
# print(random_float) 

# list

# list=["delhi","uttarpradesh"]

# list.append("goa")
# list.extend(["kashmire","punjab"])


# print(list)

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# horizontal=int(position[0])
# vertical=int(position[1])


# select_row=map[vertical-1]
# select_row[horizontal-1]="X"


# rock paper and scissor



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

game_image=[rock,paper,scissors]
user_choice =int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissor.\n"))
if user_choice >=3 or user_choice<0:
    print("invalid number")
else:
    print(game_image[user_choice])


    computer_choice=random.randint(0,2)
    print("computer choice:")
    print(game_image[computer_choice])


    if user_choice==0 and computer_choice==2:
        print("you win!")
    elif computer_choice > user_choice:
        print("you lose!")
    elif user_choice > computer_choice:
        print("you win!")    
    elif computer_choice==0 and user_choice==2:
        print("you lose!") 
    elif computer_choice==user_choice:
        print("its a draw!")    
    else:
        print("invalid number!!!!")

