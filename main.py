import turtle
from turtle import Turtle,Screen
import pandas
import pandas as pd

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
game = True
score = 0

while game:
 guessed_state = screen.textinput(title=f"Guess the State {score}/50",prompt = "Whats another states name?").title()
 if guessed_state == "Exit":
     missing_states = []
     for state in all_states:
         if state not in guessed_states:
             missing_states.append(state)
     new_data = pandas.DataFrame(missing_states)
     new_data.to_csv("states_to_learn.csv")
 if guessed_state in all_states:
     guessed_states.append(guessed_state)
     print(guessed_state)
     print(guessed_states)
     if guessed_state != guessed_states:
          print("kek")
          score+=1
 for obj in guessed_states:
     t = Turtle()
     position_row =data[data.state == obj]
     t.penup()
     t.goto(position_row.x.item(),position_row.y.item())
     t.write(obj, font=("Arial", 8, "normal"))
     t.hideturtle()



screen.exitonclick()
