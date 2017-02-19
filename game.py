from field import Field
from player import Player


class Game:
    def __init__(self):
        player1 = input('Enter the name of the first player: ')
        player2 = input('Enter the name of the second player: ')
        self._field = [Field(), Field()]
        self._players = [Player(player1), Player(player2)]
        self._current_player = 0

    def read_position(self, player):
        return self._players[player].read_position()

    def field_without_ships(self, player):
        return self._field[player].field_without_ships()

    def field_with_ships(self, player):
        return self._field[player].field_with_ships()

    def game(self):
        while(True):
            count1 = 0
            count2 = 0
            print(self._field[self._current_player].field_with_ships(),
                  self._field[1-self._current_player].field_without_ships(), sep='\n\n')
            res = self._field[1-self._current_player].shoot_at(self.read_position(self._current_player))
            if res == 2:
                print("Well done, you destroyed a ship!")
                if self._current_player == 0:
                    count1 += 1
                else:
                    count2 += 1
            elif res:
                print("Well done, you hit a ship!")
            else:
                print("Ouch, you missed!")
                self._current_player = 1 - self._current_player
                continue
            if count1 == 10:
                print("{} wins".format(self._players[0]))
                break
            if count2 == 10:
                print("{} wins".format(self._players[1]))
                break

if __name__ == "__main__":
    result = Game()
    print(result.game())
