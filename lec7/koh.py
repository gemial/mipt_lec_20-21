from turtle import *

def draw_line(length, deep):
    if deep == 1:
        forward(length)
        return
    length //= 3
    deep -= 1
    draw_line(length, deep)
    left(60)
    draw_line(length, deep)
    right(120)
    draw_line(length, deep)
    left(60)    
    draw_line(length, deep)

speed(0)
width(2)

'''for deep in range(1, 7):
    up()
    goto(-400, 600 - 200 * deep)
    down()
    draw_line(800, deep)
'''
up()
goto(-400, 0)
down()
draw_line(800, 6)
mainloop()
