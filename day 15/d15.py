
# from turtle import Turtle , Screen
# timmy=Turtle()
# #  a(objiect)=b(class)
# print(timmy)
#
# timmy.shape("turtle")
# timmy.color("red")
#
# timmy.forward(100 )
#
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick(

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon name",["pokemon","squate","charmander"])
table.add_column("type",["electric","water","fire"])

table.align="l"

print(table)



