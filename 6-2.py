class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, weight_per_meter, height):
        return self._width * self._length * weight_per_meter * height


road = Road(20, 5000)
print(road.weight(25, 5))
