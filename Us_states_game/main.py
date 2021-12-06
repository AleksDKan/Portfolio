import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
states_list = data["state"].tolist()

guessed_states = []
states_correct = 0

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state in states_list:
        states_correct += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{answer_state}")
        guessed_states.append(answer_state)

    if answer_state == 'Exit':
        states_to_learn = pd.DataFrame([x for x in states_list if x not in guessed_states])
        states_to_learn.to_csv("states_to_learn.csv")
        break


screen.exitonclick()

