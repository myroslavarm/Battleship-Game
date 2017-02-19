class Ship:
    def __init__(self, length):
        self.bow = (0, 0)
        self.horizontal = False
        self._length = length
        self._hit = [False] * length

    def shoot_at(self, coordinates):
        count = 0
        if self.horizontal:
            x = coordinates[0] - self.bow[0]
        else:
            x = coordinates[1] - self.bow[1]
        self._hit[x] = True
        print(x)
        if self._hit == [True] * self._length:
            return True
            #except IndexError as err:
            #    print(err)
            #    print(x)
            #    print(coordinates)
            #    print(self.bow)

    # def display_ship(self, x):
    #     if self._hit[x] == True:
