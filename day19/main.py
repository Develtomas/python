from turtle import Screen, Turtle
from random import randint

scr = Screen()
scr.setup(width=500, height=400)
bet = scr.textinput(title='Make you bet', prompt='Which color will win the race red/blue/green/yellow/orange?')
colors = ['red', 'blue', 'green', 'yellow', 'orange']
race_starts = False


def create_turtles(col):
    start_x = -240
    start_y = -100
    diff_y = 50
    turtles =[]
    for c in range(5):
        ti = Turtle(shape='turtle')
        ti.penup()
        ti.color(col[c])
        ti.goto(start_x, start_y + diff_y * c)
        turtles.append(ti)
    return turtles


def move_turtle(turt):
    for turtle in turt:
        if turtle.xcor() >= 230:
            return turtle.pencolor()
        else:
            rand_dist = randint(1, 10)
            turtle.forward(rand_dist)
    return False


if bet:
    race_starts = True
    all_turtles = create_turtles(colors)
    while race_starts:
        winner = move_turtle(all_turtles)
        if winner and winner == bet.lower():
            print(f'You won your bet! The winner is {winner}')
            race_starts = False
        elif winner and winner != bet.lower():
            print(f'Your bet loose! The winner is {winner}')
            race_starts = False
    scr.exitonclick()

