import turtle
import pandas

data = pandas.read_csv('50_states.csv')

correct_states = 0

screen = turtle.Screen()
screen.title('Us Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()
answers = []
all_states = data.state.to_list()
while True:
    answer_state = screen.textinput(title=f'{correct_states}/50 Correct States', prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in answers:
        state_number = all_states.index(answer_state)
        turtle.goto(data.x[state_number], data.y[state_number])
        turtle.write(data.state[state_number], True, align='center', font=('Comic Sans MS', 8, 'normal'))
        answers.append(answer_state)
        correct_states += 1

