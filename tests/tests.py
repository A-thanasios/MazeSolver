import unittest

from screen.graphic.cell import Cell
from screen.maze import Maze
from screen.graphic.point import Point
from screen.window import Window

win = Window(800, 600)


class TestMaze(unittest.TestCase):
    def test_maze_creation(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertEqual(len(maze.cells), num_rows)
        self.assertEqual(len(maze.cells[0]), num_cols)

    def test_maze_creation_with_window(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y, win)
        self.assertEqual(len(maze.cells), num_rows)
        self.assertEqual(len(maze.cells[0]), num_cols)

    def test_maze_creation_with_entrance_and_exit(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y, win)
        self.assertEqual(maze.cells[0][0].has_top_wall, False)
        self.assertEqual(maze.cells[-1][-1].has_bottom_wall, False)

class TestCell(unittest.TestCase):
    def test_cell_creation(self):
        cell = Cell((Point(0, 0), Point(50, 50)), win)
        cell.draw()
        self.assertEqual(len(cell.lines), 4)

    def test_cell_line_deletion(self):
        cell = Cell((Point(0, 0), Point(50, 50)), win)
        cell.draw()
        cell.break_wall("left")
        cell.draw()
        self.assertEqual(len(cell.lines), 3)
