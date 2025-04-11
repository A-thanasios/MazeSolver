from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=1)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.root.state = True

        while self.root.state:
            self.redraw()

    def close(self):
        self.root.state = False
