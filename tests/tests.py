import unittest

from screen.maze import Maze
from screen.graphic.point import Point
from screen.window import Window


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