from bike import Bike

bike_1 = Bike("Mountain", "Monark", "Blue")
bike_2 = Bike("Street", "Monark", "Red")

print(bike_1.model)
print(bike_1.fabricant)
print(bike_1.color)

bike_1.ride()
bike_1.stop()

print(bike_2.model)
print(bike_2.fabricant)
print(bike_2.color)

bike_2.ride()
bike_2.stop()