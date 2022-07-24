import colorgram
import turtle as t
import random as r

t.colormode(255)
SC = t.Screen()
COL_COUNT = 24
SQUARE_SIDE = 10


def extract_colors():
    colors = colorgram.extract('./img/hirst.jpg', COL_COUNT)
    rgb_colors = []
    for c in range(COL_COUNT):
        r = colors[c].rgb.r
        g = colors[c].rgb.g
        b = colors[c].rgb.b
        rgb_color = (r, g, b)
        rgb_colors.append(rgb_color)
    return rgb_colors


def draw(colors, size):
    tur = t.Turtle()
    tur.hideturtle()
    tur.penup()
    tur.goto(-200, -200)
    for i in range(size):
        for j in range(size):
            tur.dot(20, r.choice(colors))
            tur.forward(50)
        tur.setposition(-200, -200 + 50 * (i+1))


draw(extract_colors(), 10)
SC.exitonclick()
