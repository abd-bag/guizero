from tkinter import Canvas, BOTH, ALL
from . import utilities as utils
from .base import Widget
from .event import EventManager

class Drawing(Widget):

    def __init__(self, master, height=100, width=100, grid=None, align=None, command=None, visible=True, enabled=None, bg=None):

        description = "[Drawing] object"

        tk = Canvas(master.tk, height=100, width=100, bd=0, highlightthickness=0)

        super(Drawing, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

    def line(self, x1, y1, x2, y2, color="black", width=1):
        self.tk.create_line(
            x1, y1, x2, y2, 
            width = width,
            fill = "" if color is None else utils.convert_color(color)
            )

    def oval(self, x1, y1, x2, y2, color="black", outline=False, outline_color="black"):
        self.tk.create_oval(
            x1, y1, x2, y2, 
            outline = utils.convert_color(outline_color) if outline else "",
            width = int(outline),
            fill = "" if color is None else utils.convert_color(color)
            )

    def rectangle(self, x1, y1, x2, y2, color="black", outline=False, outline_color="black"):
        self.tk.create_rectangle(
            x1, y1, x2, y2, 
            outline = utils.convert_color(outline_color) if outline else "",
            width = int(outline),
            fill = "" if color is None else utils.convert_color(color)
            )

    def circle_old(self, x, y, radius, width=1, color="black", fill_color=None):
        
        self.tk.create_oval(
            x - radius, y - radius, 
            x + radius, y + radius,
            outline = "" if color is None else color,
            width = 0 if width is None else width,
            fill = "" if fill_color is None else fill_color
            )

    def clear(self):
        self.tk.delete(ALL)