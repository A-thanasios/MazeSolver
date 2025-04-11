from .point import Point
from .line import Line


class Cell(Line):
    def __init__(self, win, point1, point2,
                 has_left_wall=True, 
                 has_right_wall=True, 
                 has_top_wall=True, 
                 has_bottom_wall=True):
        super().__init__(win.canvas, "black", point1, point2)
        self.win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def __str__(self):
        return f"Cell(has_left_wall={self.has_left_wall}, has_right_wall={self.has_right_wall}, has_top_wall={self.has_top_wall}, has_bottom_wall={self.has_bottom_wall})"

    def draw(self):
        if self.has_left_wall:
            self.win.draw_line(self.make_line(self.get_left_bottom_point(), self.get_left_top_point()))
        if self.has_right_wall:
            self.win.draw_line(self.make_line(self.get_right_bottom_point(), self.get_right_top_point()))
        if self.has_top_wall:
            self.win.draw_line(self.make_line(self.get_left_top_point(), self.get_right_top_point()))
        if self.has_bottom_wall:
            self.win.draw_line(self.make_line(self.get_left_bottom_point(), self.get_right_bottom_point()))
            
    def make_line(self, point1, point2):
        return Line(self.win.canvas, self.color, 
                                    point1, point2)
    def get_left_bottom_point(self):
        return Point(self.point1.x, self.point1.y)
    def get_right_bottom_point(self):
        return Point(self.point2.x, self.point1.y)
    def get_left_top_point(self):
        return Point(self.point1.x, self.point2.y)
    def get_right_top_point(self):
        return Point(self.point2.x, self.point2.y)