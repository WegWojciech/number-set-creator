from tkinter import *
import tkinter.font as font
from pathlib import Path

# Create r x c array filled with zeros
rows = int(input("rows = "))
columns = int(input("columns = "))
array_main = [[0] * columns for i in range(rows)]
number = '10'


def get_place(r, c):
    # change button color and value in array
    if array_main[r][c] == 0:
        buttons[r][c].config(bg="black")
        array_main[r][c] = 1
    else:
        buttons[r][c].config(bg="white")
        array_main[r][c] = 0


#remove unnecesary characters and write to file
def save():
    global array_main
    for x in array_main:
        result = str(x)
        result = result.replace('[', '')
        result = result.replace(']', '')
        result = result.replace(',', '')
        file.write(result + '\n')
    file.write('\n')
    reset()


#reset the board without saving
def reset():
    # clean main array
    global array_main
    array_main = [[0] * columns for i in range(rows)]
    # clean board
    for r in range(rows):
        for c in range(columns):
            buttons[r][c].config(bg="white")


# get a set number for file name
# checks if number is in range and sets file name
while not number.isdigit() or int(number) not in range(10):
    number = (input("nr = "))
name = number + '.txt'
p = Path(__file__).with_name(name)
#file = open(name, "a")
file = p.open('a')


root = Tk()
root.title("Data Set Creation Tool")

set_font = font.Font(size=20, weight='bold')

# create button table for input
buttons = [[0] * columns for i in range(rows)]
for row in range(rows):
    for col in range(columns):
        buttons[row][col] = Button(root, width=10, height=5, bg="white", command=lambda r=row, c=col: get_place(r, c))
        buttons[row][col].grid(row=row, column=col)


# Buttons for controlling app
button_save = Button(root, width=10, height=2, bg="blue", fg='white', text='save', command=save)
button_save['font'] = set_font
button_save.grid(row=0, column=5)

button_reset = Button(root, width=10, height=2, bg="blue", fg='white', text='reset', command=reset)
button_reset['font'] = set_font
button_reset.grid(row=1, column=5)
root.mainloop()
