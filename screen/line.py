from point import Point


class Line(Point):
    def __init__(self, canvas, color, x1, y1, x2, y2):
        self.canvas = canvas
        self.color = color
        self.point1 = Point(x1, y1)
        self.point2 = Point(x2, y2)

    def draw(self):
        self.canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=self.color, width=2)

    def __str__(self):
        return f"Line(point1={self.point1}, point2={self.point2}, color={self.color})"