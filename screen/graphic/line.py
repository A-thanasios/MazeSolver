from .point import Point


class Line():
    def __init__(self, canvas, color, point1, point2):
        self.canvas = canvas
        self.color = color
        self.point1 = point1
        self.point2 = point2

    def draw(self):
        self.canvas.create_line(self.point1.x, self.point1.y, 
                                self.point2.x, self.point2.y, 
                                fill=self.color, width=2)
        
    
    def delete(self):
        if hasattr(self, 'canvas') and self.canvas:
            self.canvas.delete(self)
        # Clear references
        self.canvas = None
        self.point1 = None
        self.point2 = None

    def __str__(self):
        return f"Line(point1={self.point1}, point2={self.point2}, color={self.color})"