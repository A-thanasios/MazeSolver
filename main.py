from screen.window import Window
from screen.graphic.line import Line
from screen.graphic.cell import Cell
from screen.graphic.point import Point
win = Window(800, 600)

cell = Cell(win=win, point1=Point(100, 100), point2=Point(50, 50))
cell2 = Cell(win=win, point1=Point(200, 200), point2=Point(100, 100))
cell.draw()
cell2.draw()
cell.draw_move(cell2)

win.wait_for_close()