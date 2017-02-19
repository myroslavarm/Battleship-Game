from ship import Ship
from random import randint


def generate_field():
    '''
    () -> (list)
    This function generates the field for the game.
    '''
    ships = [[None] * 10 for i in range(10)]
    for i in range(4, 0, -1):
        for j in range(5 - i):
            while True:
                x = randint(0, 10 - i)
                y = randint(0, 10 - i)
                x1 = randint(0, 1)
                y1 = 1 - x1
                length = i
                if isEmpty(x, y, i, x1, y1, ships):
                    break
            ship = Ship(length)
            ship.bow = (y, x)
            ship.horizontal = True if x1 else False
            for n in range(-1, 1 + i):
                try:
                    coord1 = y + n * y1
                    coord2 = x + n * x1
                    if n == -1 or n == i:
                        ships[coord1][coord2] = -1
                    else:
                        ships[coord1][coord2] = ship
                    if x1 == 0:
                        if y == 0 and n == -1:
                            continue
                        if x != 0:
                            ships[coord1][coord2 - 1] = -1
                        ships[coord1][coord2 + 1] = -1
                    elif y1 == 0:
                        if x == 0 and n == -1:
                            continue
                        if y != 0:
                            ships[coord1 - 1][coord2] = -1
                        ships[coord1 + 1][coord2] = -1
                except IndexError:
                    continue
    for i in range(10):
        for j in range(10):
            if ships[i][j] == -1:
                ships[i][j] = None
    return ships


def isEmpty(x, y, n, x1, y1, data):
    '''
    This function checks whether the square is empty.
    '''
    s = 0
    for i in range(n):
        if data[y + i * y1][x + i * x1] == None:
            s += 1
    if s == n:
        return True
    else:
        return False


class Field:
    def __init__(self):
        self._ships = generate_field()
        self.shots = set()

    def shoot_at(self, coordinates):
        '''
        Checks whether the ship was destroyed, hit, or whether the player missed.
        '''
        if coordinates in self.shots:
            return -1
        self.shots.add(coordinates)
        if isinstance(self._ships[coordinates[0]][coordinates[1]], Ship):
            destroyed = self._ships[coordinates[0]][coordinates[1]].shoot_at(coordinates)
            if destroyed:
                return 2
            return True
        else:
            return False

    def field_with_ships(self):
        '''
        Returns the field where the ships are shown.
        '''
        a = '  A B C D E F G H I J\n'
        for i in range(10):
            a += str(i + 1) + ' ' if i + 1 < 10 else str(i + 1)
            for j in range(10):
                if (i, j) in self.shots:
                    if isinstance(self._ships[i][j], Ship):
                        a += 'X '
                    else:
                        a += 'O '
                else:
                    if isinstance(self._ships[i][j], Ship):
                        a += '* '
                    else:
                        a += '  '
            a += '\n'
        return a

    def field_without_ships(self):
        '''
        Returns the field where the ships are hidden.
        '''
        a = '  A B C D E F G H I J\n'
        for i in range(10):
            a += str(i + 1) + ' ' if i + 1 < 10 else str(i + 1)
            for j in range(10):
                if (i, j) in self.shots:
                    if isinstance(self._ships[i][j], Ship):
                        a += 'X '
                    else:
                        a += 'O '
                else:
                    a += '  '
            a += '\n'
        return a


if __name__ == "__main__":
    f = Field()
    print(f.field_with_ships())
