import random

class Ship:
    def __init__(self, size):
        self.row = random.randrange(0, 9)
        self.col = random.randrange(0, 9)
        self.size = size
        self.orientation = random.choice(['h', 'v'])
        self.indexes = self.compute_indexes()

    def compute_indexes(self):
        start_index = self.row * 10 + self.col
        if self.orientation == 'h':
            return [start_index + i for i in range(self.size)]
        elif self.orientation == 'v':
            return [start_index + i * 10 for i in range(self.size)]


class Player:
    def __init__(self):
        self.ships = []
        self.search = ['U' for i in range(100)] # "U" for unknown
        self.place_ships(sizes = [5, 4, 3, 2, 1])
        list_of_lists = [ship.indexes for ship in self.ships]
        self.indexes = [index for sublist in list_of_lists for index in sublist]

    def place_ships(self, sizes):
        for size in sizes:
            placed = False
            while not placed:

                # create a new ship
                ship = Ship(size)

                # check if placement is possible
                possible = True
                for i in ship.indexes:

                    # indexes must be < 100:
                    if i >= 100:
                        possible = False
                        break

                    # ships cannot behave like the 'snake'
                    new_row = 1 // 10
                    new_col = i % 10
                    if new_row != ship.row and new_col != ship.col:
                        possible = False
                        break

                    # ships cannot intersect
                    for other_ship in self.ships:
                        if i in other_ship.indexes:
                            possible = False
                            break

                # place the ship
                if possible:
                    self.ships.append(ship)
                    placed = True

    def show_ships(self):
        indexes = []

p = Player()
print(p.indexes)