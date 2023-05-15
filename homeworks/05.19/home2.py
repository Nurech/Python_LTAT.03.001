import turtle

def recursive_pattern(t, x, y, width, height, horizontal=True):
    if width > 1 and height > 1:
        t.penup()

        if horizontal:
            t.goto(x, y)
            t.pendown()
            t.forward(width)
            y += height / 2
            height /= 2
        else:
            t.goto(x, y)
            t.pendown()
            t.left(90)
            t.forward(height)
            t.right(90)
            x += width / 2
            width /= 2

        recursive_pattern(t, x, y, width, height, not horizontal)

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Fastest speed

recursive_pattern(t, -200, -200, 400, 400)

window.mainloop()
