import turtle
import pandas as pd
from state_name import State_Name

# Initialize screen & turtles
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Import data via pandas
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
coords_list = data[["x", "y"]]
coords = list(coords_list.to_records(index=False))
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()
    # for state in all_states:
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state_coord = (int(state_data.x), int(state_data.y))
        # print(answer_state, state_coord)
        state_name = State_Name(state=answer_state, coordinates=state_coord)
