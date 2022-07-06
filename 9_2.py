class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.density = 25  # kg/(m2 cm)

    def mass(self, thickness):
        # thickness [cm]
        square = self._length*self._width
        return square * self.density * thickness / 1000

r1 = Road(20,5000)
print(f"Потребуется асфальта: {r1.mass(5)}т")