# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(242, 243, 245), (231, 229, 225), (236, 243, 240), (243, 237, 242), (199, 159, 114), (69, 91, 129), (148, 85, 52), (218, 210, 115), (136, 160, 193), (27, 32, 47), (179, 161, 35), (58, 33, 22), (184, 145, 164), (123, 70, 93), (137, 175, 153), (76, 115, 78), (143, 25, 15), (61, 30, 41), (187, 97, 82), (120, 28, 43), (46, 59, 94), (99, 118, 172), (178, 96, 114), (33, 51, 44), (99, 159, 85), (66, 84, 23), (215, 174, 192), (217, 181, 172), (218, 206, 7), (159, 210, 191)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.speed(500)
tim.setheading(0)
tim.hideturtle()
number_of_dots = 101

for dot_count in range(1, number_of_dots):

    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count %  10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
