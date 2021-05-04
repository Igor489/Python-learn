class Road:

    MASS_PER_ONE_SQUARE_METRE = 25

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_asphalt_mass(self, height):
        return self.length * self.width * self.MASS_PER_ONE_SQUARE_METRE * height

road = Road(5000, 20)
print(road.get_asphalt_mass(5)/1000, 'т.')
