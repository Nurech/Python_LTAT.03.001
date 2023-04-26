import tkinter as tk

def draw_house(canvas):
    canvas.create_rectangle(50, 100, 150, 200, fill="gray")
    canvas.create_polygon(50, 100, 150, 100, 100, 50, fill="brown")
    canvas.create_rectangle(90, 150, 110, 200, fill="black")
    canvas.create_rectangle(60, 130, 80, 150, fill="blue")
    canvas.create_rectangle(120, 130, 140, 150, fill="blue")

root = tk.Tk()
root.title("House")
root.geometry("350x350")

canvas = tk.Canvas(root, width=350, height=350, bg="white")
canvas.pack()

draw_house(canvas)

root.mainloop()
