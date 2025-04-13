import random
import time
from .graphic.point import Point
from .graphic.cell import Cell


class Maze:
    def __init__(self, point, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.win = win
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        # 2D array of cells (rows x cols)
        self.cells = [[None for _ in range(num_cols)] for _ in range(num_rows)] 
        self.point = self.starting_point(point)
        self.create_cells()
        self.seed = seed if not seed else random.seed(seed)

    def create_cells(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col] = Cell(self.make_points(row, col),
                                             row, col,                                   
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

    def break_walls(self, cell):
        cell.visited = True
        while True:
            cells = []
            neighbors = self.get_unvisited_neighbors(cell)
            if len(neighbors) == 0:
                return
            next_cell = random.choice(neighbors)
            self.break_wall(cell, next_cell)
            self.draw_cells(cell.row, cell.col)
            self.draw_cells(next_cell.row, next_cell.col)
            self.animate()
            self.break_walls(next_cell)

    def solve(self, cell=None):
        if not cell:
            cell = self.cells[0][0]

        self.animate()
        cell.visited = True
        
        # If we've reached the exit cell, return True
        if cell == self.cells[-1][-1]:
            return True
            
        neighbors = self.get_unvisited_neighbors(cell)
        for neighbor in neighbors:
            if not self.wall_between(cell, neighbor):
                # Try to solve from the neighbor
                if self.solve(neighbor):
                    cell.draw_move(neighbor, True)
                    return True
                else:
                    cell.draw_move(neighbor)
        
        # If we've tried all neighbors and none led to the exit
        return False

    def get_unvisited_neighbors(self, cell):
        neighbors = []
        if cell.row - 1 >= 0 and not self.cells[cell.row - 1][cell.col].visited:
            neighbors.append(self.cells[cell.row - 1][cell.col])

        if cell.row + 1 < self.num_rows and not self.cells[cell.row + 1][cell.col].visited:
            neighbors.append(self.cells[cell.row + 1][cell.col])

        if cell.col - 1 >= 0 and not self.cells[cell.row][cell.col - 1].visited:
            neighbors.append(self.cells[cell.row][cell.col - 1])

        if cell.col + 1 < self.num_cols and not self.cells[cell.row][cell.col + 1].visited:
            neighbors.append(self.cells[cell.row][cell.col + 1])
        
        return neighbors
        
    def break_wall(self, cell, next_cell):
        if cell.row == next_cell.row:
            if cell.col > next_cell.col:
                cell.break_wall("left")
                next_cell.break_wall("right")
            else:
                cell.break_wall("right")
                next_cell.break_wall("left")
        else:
            if cell.row > next_cell.row:
                cell.break_wall("top")
                next_cell.break_wall("bottom")
            else:
                cell.break_wall("bottom")
                next_cell.break_wall("top")

    def wall_between(self, cell, neighbor):
        if cell.row == neighbor.row:
            if cell.col > neighbor.col:
                return cell.has_left_wall or neighbor.has_right_wall
            else:
                return cell.has_right_wall or neighbor.has_left_wall
        else:
            if cell.row > neighbor.row:
                return cell.has_top_wall or neighbor.has_bottom_wall
            else:
                return cell.has_bottom_wall or neighbor.has_top_wall

    def reset_cells_visited(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col].visited = False
                
        
    def animate(self):
        if self.win:
            self.win.redraw()
        time.sleep(0.02)

    def starting_point(self, point):
        return (point / 2) - Point(self.cell_size_x * self.num_rows / 2,
                                    self.cell_size_y * self.num_cols / 2)

    def make_points(self, row, col):
        return (Point(self.point.x + col * self.cell_size_x, 
                     self.point.y + row * self.cell_size_y), 
                Point(self.point.x + (col + 1) * self.cell_size_x, 
                     self.point.y + (row + 1) * self.cell_size_y))