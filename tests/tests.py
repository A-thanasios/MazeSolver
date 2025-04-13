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
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertEqual(maze.cells[0][0].has_top_wall, False)
        self.assertEqual(maze.cells[-1][-1].has_bottom_wall, False)

    def test_maze_get_unvisited_neighbours(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        # Test top-left corner cell (0,0)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[0][0]), [maze.cells[0][1], maze.cells[1][0]])
        
        # Test middle cell (5,5)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[5][5]), 
                            [maze.cells[4][5], maze.cells[6][5], maze.cells[5][4], maze.cells[5][6]])
        
        # Test right edge cell (5,11)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[5][11]), 
                            [maze.cells[4][11], maze.cells[6][11], maze.cells[5][10]])
        
        # Test bottom edge cell (9,5)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[9][5]), 
                            [maze.cells[8][5], maze.cells[9][4], maze.cells[9][6]])
        
        # Test bottom-right corner cell (9,11)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[9][11]), 
                            [maze.cells[8][11], maze.cells[9][10]])

    def test_maze_get_unvisited_neighbours_corner_cells(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        # Test top-left corner cell (0,0)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[0][0]), [maze.cells[0][1], maze.cells[1][0]])
        
        # Test bottom-right corner cell (9,11)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[9][11]), 
                            [maze.cells[8][11], maze.cells[9][10]])

    def test_maze_get_unvisited_neighbours_edge_cells(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        # Test right edge cell (5,11)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[5][11]), 
                            [maze.cells[4][11], maze.cells[6][11], maze.cells[5][10]])
        
        # Test bottom edge cell (9,5)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[9][5]), 
                            [maze.cells[8][5], maze.cells[9][4], maze.cells[9][6]])

    def test_maze_get_unvisited_neighbours_middle_cells(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        # Test center cell (5,5)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[5][5]), 
                            [maze.cells[4][5], maze.cells[6][5], maze.cells[5][4], maze.cells[5][6]])
        
        # Test cell near top (2,5)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[2][5]), 
                            [maze.cells[1][5], maze.cells[3][5], maze.cells[2][4], maze.cells[2][6]])
        
        # Test cell near left (5,2)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[5][2]), 
                            [maze.cells[4][2], maze.cells[6][2], maze.cells[5][1], maze.cells[5][3]])
        
        # Test cell near center (4,6)
        self.assertCountEqual(maze.get_unvisited_neighbors(maze.cells[4][6]), 
                            [maze.cells[3][6], maze.cells[5][6], maze.cells[4][5], maze.cells[4][7]])

    def test_maze_break_wall_horizontal(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test breaking right wall
        cell1 = maze.cells[5][5]
        cell2 = maze.cells[5][6]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_right_wall, False)
        self.assertEqual(cell2.has_left_wall, False)
        
        # Test breaking left wall
        cell1 = maze.cells[5][6]
        cell2 = maze.cells[5][5]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_left_wall, False)
        self.assertEqual(cell2.has_right_wall, False)

    def test_maze_break_wall_vertical(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test breaking bottom wall
        cell1 = maze.cells[5][5]
        cell2 = maze.cells[6][5]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_bottom_wall, False)
        self.assertEqual(cell2.has_top_wall, False)
        
        # Test breaking top wall
        cell1 = maze.cells[6][5]
        cell2 = maze.cells[5][5]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_top_wall, False)
        self.assertEqual(cell2.has_bottom_wall, False)

    def test_maze_break_wall_corner_cases(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test breaking walls at maze edges
        # Top edge
        cell1 = maze.cells[0][5]
        cell2 = maze.cells[1][5]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_bottom_wall, False)
        self.assertEqual(cell2.has_top_wall, False)
        
        # Left edge
        cell1 = maze.cells[5][0]
        cell2 = maze.cells[5][1]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_right_wall, False)
        self.assertEqual(cell2.has_left_wall, False)

    def test_maze_break_wall_horizontal_right(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test breaking wall when moving right (cell1 to cell2)
        cell1 = maze.cells[5][5]
        cell2 = maze.cells[5][6]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_right_wall, False)
        self.assertEqual(cell2.has_left_wall, False)
        # Verify other walls remain intact
        self.assertEqual(cell1.has_left_wall, True)
        self.assertEqual(cell1.has_top_wall, True)
        self.assertEqual(cell1.has_bottom_wall, True)
        self.assertEqual(cell2.has_right_wall, True)
        self.assertEqual(cell2.has_top_wall, True)
        self.assertEqual(cell2.has_bottom_wall, True)

    def test_maze_break_wall_horizontal_left(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test breaking wall when moving left (cell1 to cell2)
        cell1 = maze.cells[5][6]
        cell2 = maze.cells[5][5]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_left_wall, False)
        self.assertEqual(cell2.has_right_wall, False)
        # Verify other walls remain intact
        self.assertEqual(cell1.has_right_wall, True)
        self.assertEqual(cell1.has_top_wall, True)
        self.assertEqual(cell1.has_bottom_wall, True)
        self.assertEqual(cell2.has_left_wall, True)
        self.assertEqual(cell2.has_top_wall, True)
        self.assertEqual(cell2.has_bottom_wall, True)

    def test_maze_break_wall_vertical_down(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test breaking wall when moving down (cell1 to cell2)
        cell1 = maze.cells[5][5]
        cell2 = maze.cells[6][5]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_bottom_wall, False)
        self.assertEqual(cell2.has_top_wall, False)
        # Verify other walls remain intact
        self.assertEqual(cell1.has_top_wall, True)
        self.assertEqual(cell1.has_left_wall, True)
        self.assertEqual(cell1.has_right_wall, True)
        self.assertEqual(cell2.has_bottom_wall, True)
        self.assertEqual(cell2.has_left_wall, True)
        self.assertEqual(cell2.has_right_wall, True)

    def test_maze_break_wall_vertical_up(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test breaking wall when moving up (cell1 to cell2)
        cell1 = maze.cells[6][5]
        cell2 = maze.cells[5][5]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_top_wall, False)
        self.assertEqual(cell2.has_bottom_wall, False)
        # Verify other walls remain intact
        self.assertEqual(cell1.has_bottom_wall, True)
        self.assertEqual(cell1.has_left_wall, True)
        self.assertEqual(cell1.has_right_wall, True)
        self.assertEqual(cell2.has_top_wall, True)
        self.assertEqual(cell2.has_left_wall, True)
        self.assertEqual(cell2.has_right_wall, True)

    def test_maze_break_wall_edge_cases(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test breaking walls at maze edges
        # Top edge moving down
        cell1 = maze.cells[0][5]
        cell2 = maze.cells[1][5]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_bottom_wall, False)
        self.assertEqual(cell2.has_top_wall, False)
        
        # Left edge moving right
        cell1 = maze.cells[5][0]
        cell2 = maze.cells[5][1]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_right_wall, False)
        self.assertEqual(cell2.has_left_wall, False)
        
        # Bottom edge moving up
        cell1 = maze.cells[num_rows-1][5]
        cell2 = maze.cells[num_rows-2][5]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_top_wall, False)
        self.assertEqual(cell2.has_bottom_wall, False)
        
        # Right edge moving left
        cell1 = maze.cells[5][num_cols-1]
        cell2 = maze.cells[5][num_cols-2]
        maze.break_wall(cell1, cell2)
        self.assertEqual(cell1.has_left_wall, False)
        self.assertEqual(cell2.has_right_wall, False)

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Mark some cells as visited
        maze.cells[0][0].visited = True
        maze.cells[5][5].visited = True
        maze.cells[num_rows-1][num_cols-1].visited = True
        
        # Verify cells are marked as visited
        self.assertTrue(maze.cells[0][0].visited)
        self.assertTrue(maze.cells[5][5].visited)
        self.assertTrue(maze.cells[num_rows-1][num_cols-1].visited)
        
        # Reset visited states
        maze.reset_cells_visited()
        
        # Verify all cells are marked as unvisited
        for row in range(num_rows):
            for col in range(num_cols):
                self.assertFalse(maze.cells[row][col].visited)

    def test_maze_reset_cells_visited_after_maze_generation(self):
        # Use a smaller maze to avoid recursion issues
        num_cols = 3
        num_rows = 3
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Generate maze (this will mark cells as visited)
        maze.break_walls(maze.cells[0][0])
        
        # Reset visited states
        maze.reset_cells_visited()
        
        # Verify all cells are marked as unvisited
        for row in range(num_rows):
            for col in range(num_cols):
                self.assertFalse(maze.cells[row][col].visited)

    def test_maze_reset_cells_visited_partial_maze(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Mark a specific path as visited
        path = [
            (0, 0), (0, 1), (0, 2),
            (1, 2), (2, 2), (2, 1)
        ]
        for row, col in path:
            maze.cells[row][col].visited = True
        
        # Reset visited states
        maze.reset_cells_visited()
        
        # Verify all cells are marked as unvisited
        for row in range(num_rows):
            for col in range(num_cols):
                self.assertFalse(maze.cells[row][col].visited)

    def test_wall_between_horizontal_neighbors(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test cells in the same row
        cell1 = maze.cells[5][5]
        cell2 = maze.cells[5][6]
        
        # Initially, all walls should be present
        self.assertTrue(maze.wall_between(cell1, cell2))
        
        # Break the wall between them
        maze.break_wall(cell1, cell2)
        
        # Now there should be no wall between them
        self.assertFalse(maze.wall_between(cell1, cell2))
        
    def test_wall_between_vertical_neighbors(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 50
        cell_size_y = 50
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_size_x, cell_size_y)
        
        # Test cells in the same column
        cell1 = maze.cells[5][5]
        cell2 = maze.cells[6][5]
        
        # Initially, all walls should be present
        self.assertTrue(maze.wall_between(cell1, cell2))
        
        # Break the wall between them
        maze.break_wall(cell1, cell2)
        
        # Now there should be no wall between them
        self.assertFalse(maze.wall_between(cell1, cell2))
        



class TestCell(unittest.TestCase):
    def test_cell_creation(self):
        cell = Cell((Point(0, 0), Point(50, 50)), 0, 0)
        self.assertEqual(cell.has_left_wall, True)
        self.assertEqual(cell.has_right_wall, True)
        self.assertEqual(cell.has_top_wall, True)
        self.assertEqual(cell.has_bottom_wall, True)

    def test_cell_wall_breaking(self):
        cell = Cell((Point(0, 0), Point(50, 50)), 0, 0)
        cell.break_wall("left")
        self.assertEqual(cell.has_left_wall, False)
        self.assertEqual(cell.has_right_wall, True)
        self.assertEqual(cell.has_top_wall, True)
        self.assertEqual(cell.has_bottom_wall, True)
