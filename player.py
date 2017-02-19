import string

class Player:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return '{}'.format(self._name)

    def read_position(self):
        '''
        Reads the coordinates of the shot and converts them into the correct type.
        '''
        s = input('Enter the coordinates you are aiming at: ')
        if s[0] in string.ascii_uppercase and (65 <= ord(s[0]) <= 74) and (1 <= int(s[1:]) <= 10):
            x = s[0]
            y = int(s[1:])
        else:
            s = input('The letter must be uppercase (A-J) and it must'
                      + ' be followed by a number from 1 to 10. Please try again: ')
            x = s[0]
            y = int(s[1:])
        coord = (y - 1, ord(x)-ord('A'))
        return coord
