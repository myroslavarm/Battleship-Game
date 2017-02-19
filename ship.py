class Ship:
    def __init__(self, length):
        self.bow = (0, 0)
        self.horizontal = False
        self._length = length
        self._hit = [False] * length

    def shoot_at(self, coordinates):
        '''
        Returns true if the ship was destroyed.
        '''
        if self.horizontal:
            x = coordinates[1] - self.bow[1]
        else:
            x = coordinates[0] - self.bow[0]
        self._hit[x] = True
        if sum(self._hit) == self._length:
            return True
