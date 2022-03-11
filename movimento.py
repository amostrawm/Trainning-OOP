import time


class Moving:
    def __init__(self, obj):
        self.obj = obj

    def mover(self):
        for i in range(1, 20):
            print((" " * i) + str(self.obj))
            time.sleep(.05)
        if i <= 20:
            x = 20
            for i in range(1, 20):
                print((" " * x) + str(self.obj))
                x -= 1
                time.sleep(.05)
