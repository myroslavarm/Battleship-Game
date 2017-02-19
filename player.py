class Player:
    def __init__(self, name):
        self._name = name

    def read_position(self):
        s = input('Enter the coordinates you are aiming at: ')
        x = s[0]
        y = int(s[1:])
        coord = (y - 1, ord(x)-ord('A'))
        return coord
