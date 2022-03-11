class Bike:

    def __init__(self, model, fabricant, color):
        self.model = model
        self.fabricant = fabricant
        self.color = color

    def ride(self):
        print("This " + self.model + " bike is running!")

    def stop(self):
        print("This " + self.model + " bike is stopped!")