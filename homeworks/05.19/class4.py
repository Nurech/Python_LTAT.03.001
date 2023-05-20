import turtle


def draw_fractal(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        draw_fractal(t, length / 3, depth - 1)
        t.left(85)
        draw_fractal(t, length / 3, depth - 1)
        t.right(170)
        draw_fractal(t, length / 3, depth - 1)
        t.left(85)
        draw_fractal(t, length / 3, depth - 1)


win = turtle.Screen()
win.bgcolor('white')

t = turtle.Turtle()
t.speed(0)

length = 900
depth = 3

t.penup()
t.goto(-length / 2, 0)
t.pendown()

draw_fractal(t, length, depth)

turtle.done()
