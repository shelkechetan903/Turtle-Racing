from turtle import Turtle,Screen
import random

is_game_st=False
screen=Screen()
screen.setup(width=500,height=400)

user_input=screen.textinput("Make Your Bet "," Which Turtle will Win The race, Enter Colour :")
colours=["red","yellow","green","purple","orange","blue"]
y_position=[-70,-45,-20,5,30,55]
all_turtle=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-250,y=y_position[turtle_index])
    all_turtle.append(new_turtle)
    
if user_input:
    is_game_st=True
    
while is_game_st:
    
    for t in all_turtle:
        if t.xcor()>230:
            is_game_st=False
            winning_colour=t.pencolor()
            if winning_colour == user_input:
                print(f"you Won , the Winnig Colour is {winning_colour}.")
            else:
                print(f"you lost , the Winnig Colour is {winning_colour}.")
        rand_distance=random.randint(1,10)
        t.forward(rand_distance)
screen.exitonclick()    
