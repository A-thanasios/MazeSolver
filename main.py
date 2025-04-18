from screen.maze import Maze
from screen.window import Window
from screen.graphic.line import Line
from screen.graphic.cell import Cell
from screen.graphic.point import Point

width = 1800
height = 1200
screen_size = Point(width, height)
num_rows = 20
num_cols = 20
cell_size_x = 50
cell_size_y = 50

def main():
    win = Window(width, height)

    maze = Maze(screen_size,
                num_rows, num_cols,
                cell_size_x, cell_size_y,
                win)
    maze.break_walls(maze.cells[0][0])
    maze.reset_cells_visited()
    maze.solve()
    maze.animate()
    
    
    win.wait_for_close()

if __name__ == "__main__":
    main()