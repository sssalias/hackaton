import random as rd

animal_type = ['Кошка', 'Собака']
possible_coords = [(-2450, 700), (3300, 750), (-2400, -500), (-2420, -4700), (-2200, -8100), (-1700, -9800),
                  (500, -9800), (3000, -9950), (3400, -5200), (3450, -4100), (2400, -6800), (200, -5300), (1800, -3100)]
possible_fin_coords = [(0, 0), (600, 300), (500, 200), (100, 200), (200, 50)]


class Animal:
    def __init__(self, type=rd.choice(animal_type)):
        self.type = type
        self.coords = rd.choice(possible_coords)

    def find(self):
        self.coords = rd.choice(possible_fin_coords)
