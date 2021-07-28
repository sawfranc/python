import math
from tkinter import Canvas


class GrapherException(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)


class GrapherCanvas(Canvas):

    def __init__(self, parent, width, height, background):
        Canvas.__init__(self, parent, width=width, height=height, background=background)

        self.xMin = -math.pi
        self.xMax = math.pi
        self.yMin = -1
        self.yMax = 1
        self.f = math.sin
        self.redraw(width, height)

    @property
    def xMin(self):
        return self.__xMin

    @xMin.setter
    def xMin(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise GrapherException("minimale value for abscissa must be a numeric value")
        self.__xMin = value

    @property
    def xMax(self):
        return self.__xMax

    @xMax.setter
    def xMax(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise GrapherException("maximale value for abscissa must be a numeric value")
        self.__xMax = value

    @property
    def yMin(self):
        return self.__yMin

    @yMin.setter
    def yMin(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise GrapherException("minimale value for ordinate must be a numeric value")
        self.__yMin = value

    @property
    def yMax(self):
        return self.__yMax

    @yMax.setter
    def yMax(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise GrapherException("maximale value for ordinate must be a numeric value")
        self.__yMax = value

    @property
    def f(self):
        return self.__f

    @f.setter
    def f(self, func):
        if not callable(func):
            raise GrapherException("func must be a callable element")
        self.__f = func

    def redraw(self, width=None, height=None):
        w = width or self.winfo_width()
        h = height or self.winfo_height()

        tx = lambda x: w * (x - self.xMin) / (-self.xMin + self.xMax)
        ty = lambda y: h * (1 - (y - self.yMin) / (-self.yMin + self.yMax))

        # Delete all existing graphical elements
        self.delete("all")

        # Draw origin
        self.create_line(tx(self.xMin), ty(0), tx(self.xMax), ty(0), fill="gray")
        self.create_line(tx(0), ty(self.yMin), tx(0), ty(self.yMax), fill="gray")
        self.create_text(tx(0) + 15, ty(0) + 10, text="0,0", fill="black")

        # Draw the curve
        i = self.xMin
        oldX = tx(i)
        oldY = ty(self.f(i))

        while i < self.xMax + 0.1:
            x = tx(i)
            y = ty(self.f(i))
            self.create_line(oldX, oldY, x, y, fill="red")
            oldX = x
            oldY = y
            i += 0.1