from random import *


def read_field(filename):
    '''
    (str) -> (dict)
     This functions reads from file and returns a dictionary.
    '''
    dictionary = {}
    values = {' ': 0, '*': 1, 'X': 2}
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                dictionary[(i, j)] = values[lines[i][j]]
    return dictionary


def has_ship(data, tup):
    '''
    (dict, tuple) -> (bool)
     This functions determines whether there's a ship in this square.
    '''
    # tup = (tup[1] - 1, ord(tup[0])-ord('A'))
    if data[tup] != 0:
        return True
    else:
        return False
has_ship(read_field('field.txt'), (1, 1))


def ship_size(data, tup):
    '''
    (dict, tuple) -> (tuple)
    This function determines the size of the ship.
    '''
    if has_ship(data, tup) == 0:
        return 0
    else:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        length = 1
        for d in directions:
            i = 1
            while True:
                try:
                    if data[(tup[0] + d[0]*i, tup[1] + d[1]*i)] != 0:
                        length += 1
                        i += 1
                    else:
                        break
                except:
                    break
    return length


def is_valid(data):
    '''
    (dict) -> (bool)
     This function checks whether the field is valid (suitable for the game).
    '''
    visited = set()
    my_ships = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    directions1 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(10):
        for j in range(10):
            if(data[(i, j)] != 0) and (i, j) not in visited:
                my_ships.append(ship_size(data, (i, j)))
                visited.add((i, j))
                for item in directions1:
                    try:
                        if data[(i + item[0], j + item[1])] != 0:
                            return False
                    except:
                        pass
                for direction in directions:
                    k = 1
                    while True:
                            curr = (i + k*direction[0], j + k*direction[1])
                            try:
                                if data[curr] != 0:
                                    for item in directions1:
                                        try:
                                            if data[(curr[0]+item[0], curr[1]+item[1])] != 0:
                                                return False
                                            visited.add((i + k*direction[0], j + k*direction[1]))
                                        except:
                                            pass
                                    k += 1
                                else:
                                    break
                            except:
                                break
    if sorted(list(set(my_ships))) != sorted(list(range(1, 5))):
        return False
    ships = [4, 3, 2, 1]
    for i in range(1, 5):
        if my_ships.count(i) != ships[i - 1]:
            return False
    return True


def field_to_str(data):
    '''
    (dict) -> (str)
     This function prints out the field in a string format.
    '''
    a = ""
    for i in range(10):
        for j in range(10):
            if data[(i, j)] == 0:
                a += " "
            else:
                a += "*"
        a += "\n"
    return a


def generate_field():
    '''
    () -> (list)
     This function generates the field for the game.
    '''
    data = [[' ' for i in range(10)] for j in range(10)]
    for i in range(4, 0, -1):
        for j in range(5-i):
            while True:
                x = randint(0, 10-i)
                y = randint(0, 10-i)
                x1 = randint(0, 1)
                y1 = 1 - x1
                if isEmpty(x, y, i, x1, y1, data):
                    break
            for n in range(-1, 1+i):
                try:
                    coord1 = y + n*y1
                    coord2 = x + n*x1
                    if n == -1 or n == i:
                        data[coord1][coord2] = '-'
                    else:
                        data[coord1][coord2] = '*'
                    if x1 == 0:
                        if y == 0 and n == -1:
                            continue
                        if x != 0:
                            data[coord1][coord2-1] = '-'
                        data[coord1][coord2+1] = '-'
                    elif y1 == 0:
                        if x == 0 and n == -1:
                            continue
                        if y != 0:
                            data[coord1-1][coord2] = '-'
                        data[coord1+1][coord2] = '-'
                except IndexError:
                    continue
    for i in range(10):
        for j in range(10):
            if data[i][j] == '-':
                data[i][j] = ' '
    return data


def isEmpty(x, y, n, x1, y1, data):
    '''
    This function checks whether the square is empty.
    '''
    s = 0
    for i in range(n):
        if data[y + i*y1][x + i*x1] == ' ':
            s += 1
    if s == n:
        return True
    else:
        return False


def final_result(data):
    '''
    This function is the same as field_to_str() but it works for lists.
    '''
    a = ""
    for i in range(10):
        for j in range(10):
            a += data[i][j]
        a += "\n"
    return a


data = read_field('field.txt')
print(generate_field())
print(final_result(generate_field()))
