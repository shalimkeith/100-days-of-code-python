# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.speed(1)
# timmy.shapesize(2)
# timmy.forward(100)
# print(timmy)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


from prettytable import PrettyTable

Table = PrettyTable()
Table.add_column("Name",["Pikachu","Squirtle","Charmander","Bulbasaur"])
Table.add_column("Type",["Electric","Water","Fire","Grass/Poison"])
Table.align = "l"

print(Table)
