import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # it can be any image file with .gif

# once image is added to the screen then it is ready to be used by turtle
turtle.shape(image)


'''
to find out the coordinates of the state use this

def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()  # Somehow equivalent to screen.exitonclick()
'''
# to get the input text box in the user screen

data_path = "50_states.csv"

data = pandas.read_csv(data_path)
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 State Correct", prompt="What is the state name?")
    answer = answer_state.title()
    # screen.exitonclick()

    if answer == "Exit":
        missing_states = [
            state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state)
        # It basically just grabs the first element only which will be our main data
        # t.write(state_data.state.item())
        t.write(answer)

# screen.exitonclick()
