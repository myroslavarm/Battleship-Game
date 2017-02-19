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

    def shoot_at(self, player, coordinates):
        return self._field[player].shoot_at(coordinates)

    def game(self):
        '''
        The main function that determines how the game is played.
        '''
        count1 = 0
        count2 = 0
        while(True):
            print(self.field_with_ships(self._current_player),
                  self.field_without_ships(1 - self._current_player), sep='\n\n')
            res = -1
            while res == -1:
                res = self.shoot_at(1 - self._current_player, self.read_position(self._current_player))
                if res == -1:
                    print("Try again.")
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
            print(count1, count2)
            if count1 == 10:
                return "\n{} wins!".format(self._players[0])
            if count2 == 10:
                return "\n{} wins!".format(self._players[1])

if __name__ == "__main__":
    result = Game()
    print(result.game())
