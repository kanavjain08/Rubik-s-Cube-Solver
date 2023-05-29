import tkinter as tk
import random

window = tk.Tk()
window.geometry("400x500")

colour_list = ["red", "blue", "white", "green", "yellow", "orange"]
middle_canvas_list = []
left_canvas_list = []
right_canvas_list = []

for i in range(8):
    for j in range(2):
        choose_color = random.choice(colour_list)
        canvas = tk.Canvas(window, width=50, height=50, background="red")
        canvas.grid(row=i,column=j+2)
        middle_canvas_list.append(canvas)

for i in range(2):
    for j in range(2):
        choose_color = random.choice(colour_list)
        canvas = tk.Canvas(window, width=50, height=50, background="black")
        canvas.grid(row=i+2,column=j)
        left_canvas_list.append(canvas)

for i in range(2):
    for j in range(2):
        choose_color = random.choice(colour_list)
        canvas = tk.Canvas(window, width=50, height=50, background="black")
        canvas.grid(row=i+2,column=j+4)
        right_canvas_list.append(canvas)

def mix():
    pass

def solver():
    middle_canvas_list[0].config(background="blue")

button = tk.Button(window, text="solve", command=solver)
button.grid()

window.mainloop()