# print(len())
# a=123
# print(type(a))

# a=str(123)
# print(type(a))

# a=float(123)
# print(type(a))

# print(str(70) +str(100))

# score=0
# height=1.8
# iswining=True

# #f-string

# print(f"your score is {score},ypur height is {height}, you are winning is {iswining}")


# tip calculator

print("welcome to the tip calculator")
x=float(input("what was the total bill?"))
y=int(input("what percentage tip would you like to give? 10, 12 , or 15?"))
z=int(input("how many people to split the bill?"))

tip=x*y/100
total=x-tip
total=total/z

print(f"each person should pay: {total}")

