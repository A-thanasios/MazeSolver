import time
from .graphic.point import Point
from .graphic.cell import Cell


class Maze:
    def __init__(self, point, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.win = win
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        # 2D array of cells (rows x cols)
        self.cells = [[None for _ in range(num_cols)] for _ in range(num_rows)] 
        self.point = self.starting_point(point)
        self.create_cells()

    def create_cells(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col] = Cell(self.make_points(row, col),                                   
                                       self.win)
        
        self.break_entrance_and_exit()
        
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.draw_cells(row, col)
        
    
    def draw_cells(self, row, col):
        self.cells[row][col].draw()
    
    def break_entrance_and_exit(self):
        self.cells[0][0].break_wall("top")
        self.draw_cells(0, 0)
        self.cells[-1][-1].break_wall("bottom")
        self.draw_cells(-1, -1)
        self.animate()

    def animate(self):
        if self.win:
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