from .point import Point
from .line import Line


class Cell(Line):
    def __init__(self, points, row, col, win=None,
                 has_left_wall=True, 
                 has_right_wall=True, 
                 has_top_wall=True, 
                 has_bottom_wall=True):
        super().__init__(win.canvas if win else None, "black", points[0], points[1])
        self.row = row
        self.col = col
        self.win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.lines = []
        self.visited = False


    def draw(self):
        if self.win is None:
            return
        
        # First delete all existing lines
        for line in self.lines:
            if line:
                line._Line__delete()
        self.lines.clear()  # Clear the list after deleting all lines
        
        # Then create new lines based on current wall states
        if self.has_left_wall:
            left_line = self.make_line(
                self.get_left_bottom_point(), 
                self.get_left_top_point(), 
                self.color)
            self.lines.append(left_line)
            self.win.draw_line(left_line)
            
        if self.has_right_wall:
            right_line = self.make_line(
                self.get_right_bottom_point(), 
                self.get_right_top_point(), 
                self.color)
            self.lines.append(right_line)
            self.win.draw_line(right_line)
            
        if self.has_top_wall:
            top_line = self.make_line(
                self.get_left_top_point(), 
                self.get_right_top_point(),
                self.color)
            self.lines.append(top_line)
            self.win.draw_line(top_line)
            
        if self.has_bottom_wall:
            bottom_line = self.make_line(
                self.get_left_bottom_point(), 
                self.get_right_bottom_point(), 
                self.color)
            self.lines.append(bottom_line)
            self.win.draw_line(bottom_line)
        
        # Force window update
        self.win.redraw()

    def make_line(self, point1, point2, color):
        return Line(self.win.canvas, color, 
                                    point1, point2)

    def draw_move(self, to_cell, undo=False):
        self.win.draw_line(self.make_line(self.get_center_point(),
                                           to_cell.get_center_point(), "red" if undo else "gray"))

    def break_wall(self, side):
        match side:
            case "left":
                self.has_left_wall = False
                self.draw()
            case "right":
                self.has_right_wall = False
                self.draw()
            case "top":
                self.has_top_wall = False
                self.draw()
            case "bottom":
                self.has_bottom_wall = False
                self.draw()

    def get_left_bottom_point(self):
        return Point(self.point1.x, self.point2.y)
    def get_right_bottom_point(self):
        return Point(self.point2.x, self.point2.y)
    def get_left_top_point(self):
        return Point(self.point1.x, self.point1.y)
    def get_right_top_point(self):
        return Point(self.point2.x, self.point1.y)
    def get_center_point(self):
        return Point((self.point1.x + self.point2.x) / 2, (self.point1.y + self.point2.y) / 2)
    
    def __str__(self):
        return f'Cell(row={self.row}, col={self.col})'