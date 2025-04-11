from window import Window
from line import Line

win = Window(800, 600)

line1 = Line(win.canvas, "red", 100, 100, 200, 200)
line2 = Line(win.canvas, "blue", 200, 200, 300, 300)
line3 = Line(win.canvas, "green", 300, 300, 400, 400)

win.draw_line(line1)
win.draw_line(line2)
win.draw_line(line3)
win.wait_for_close()