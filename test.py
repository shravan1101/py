class Demo:
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

d = Demo(5)
print(d.get_x())  # ❌ Method call
