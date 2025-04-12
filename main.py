from screen.maze import Maze
from screen.window import Window
from screen.graphic.line import Line
from screen.graphic.cell import Cell
from screen.graphic.point import Point

width = 1000
height = 1000
num_rows = 10
num_cols = 10
cell_size_x = width / num_cols
cell_size_y = height / num_rows

def main():
    win = Window(width, height)
    maze = Maze(win, Point(width, height), 10, 10, 50, 50)
    maze.animate()
    win.wait_for_close()

if __name__ == "__main__":
    main()