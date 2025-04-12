import time
from .graphic.point import Point
from .graphic.cell import Cell


class Maze:
    def __init__(self, win, point, num_rows, num_cols, cell_size_x, cell_size_y):
        self.win = win
        
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.cells = [[None for _ in range(num_cols)] for _ in range(num_rows)]
        self.point = self.starting_point(point)
        self.create_cells()

    def create_cells(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col] = Cell(self.win, 
                                       self.make_points(row, col), 
                                       self.cell_size_x, 
                                       self.cell_size_y)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.draw_cells(row, col)

    def draw_cells(self, row, col):
        self.cells[row][col].draw()


    def animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def starting_point(self, point):
        return (point / 2) - Point(self.cell_size_x * self.num_rows / 2,
                                    self.cell_size_y * self.num_cols / 2)

    def make_points(self, row, col):
        return (Point(self.point.x + col * self.cell_size_x, 
                     self.point.y + row * self.cell_size_y), 
                Point(self.point.x + (col + 1) * self.cell_size_x, 
                     self.point.y + (row + 1) * self.cell_size_y))