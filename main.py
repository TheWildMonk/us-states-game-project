from turtle import Turtle, Screen
import pandas as pd

# Screen object definition
screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(width=725, height=491)

# Turtle object definition
states_name = Turtle()
states_name.penup()
states_name.hideturtle()

# Read the CSV
all_states = pd.read_csv("50_states.csv")

# Begin game
user_answer = screen.textinput(title="Guess the State", prompt="What's the state?").title()
correct_answer = []
user_score = 0
end_game = False

while not end_game:
    if user_answer == "Exit":
        break
    else:
        for each_state in all_states.state:
            if user_answer == each_state:
                if user_answer in correct_answer:
                    pass
                else:
                    state = all_states[all_states.state == user_answer]
                    states_name.goto(state.x.values[0], state.y.values[0])
                    states_name.write(user_answer, align="center", font=("raleway", 6, "bold"))
                    correct_answer.append(user_answer)
                    user_score += 1

        if len(correct_answer) == 50:
            end_game = True
        else:
            user_answer = screen.textinput(title=f"{user_score}/50 States Correct",
                                           prompt="What's another state?").title()


# Screen exit
screen.exitonclick()

# Generate a CSV file with all missing states
missing_states = []
for each_state in all_states.state:
    if each_state in correct_answer:
        pass
    else:
        missing_states.append(each_state)

df_missing_states = {
    "state": missing_states,
}

pd.DataFrame(df_missing_states).to_csv("states_to_learn.csv")

