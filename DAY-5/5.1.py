# fruits=["apple","banana","orange"]

# for i in fruits :
#     print(i)


    # password generator 


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy password genertor
# password=""

# for char in range(1,nr_letters+1):
#     random_char=random.choice(letters)
#     password +=random_char

# for num in range(1,nr_numbers+1):
#     password +=random.choice(numbers)  


# for sys in range(1,nr_symbols+1):
#     password +=random.choice(symbols)


# print(password)

#hard password generator
password=[]

for char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password.append(random_char)

for num in range(1,nr_numbers+1):
    password.append(random.choice(numbers))  


for sys in range(1,nr_symbols+1):
    password.append(random.choice(symbols))


random_suffle=random.shuffle(password)
# print(password)

hard_password=""
for char in password:
    hard_password +=char

print(hard_password)    
    



