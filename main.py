import numpy as np


class Player:
    pass


# It has already become a monolithic nightmare
# Smells like cheese
def char_map(num):
    if num == 0:
        return " . "
    elif num == 1:
        return " []"
    else:
        return " @ "


class GameWorld:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Game must exist")
        self.width = width
        self.height = height

        self.world_layer = np.zeros((self.width, self.height), dtype=int)
        self.player = (0, 0)

    def __str__(self):
        ret = self.world_layer
        ret[self.player] = 5

        string = ""
        for row in ret:
            tmp = ""
            for entry in row:
                tmp = tmp + char_map(entry)
            string = string + tmp + '\n'

        return string

    def in_bounds(self, x, y):
        if x <= 0 or x >= self.width:
            return False
        if y <= 0 or y >= self.height:
            return False
        else:
            return True

    def no_collision(self, x, y):
        return self.in_bounds(x, y) and self.world_layer[(x, y)] == 0

    def player_collision(self):
        return self.world_layer[self.player] != 0

    def place_player(self, x, y):
        if self.in_bounds(x, y):
            self.player = (x, y)
            return True
        else:
            return False

    def move_player(self, direction):
        # "1,2,3,4 => left right up down"
        cord = self.player

        if direction == 1:
            cord = (cord[0] - 1, cord[1])
        elif direction == 2:
            cord = (cord[0] + 1, cord[1])
        elif direction == 3:
            cord = (cord[0], cord[1] + 1)
        elif direction == 4:
            cord = (cord[0], cord[1] - 1)

        return self.place_player(cord[0], cord[1])

    def place_object(self, x, y):
        if self.no_collision(x, y):
            self.world_layer[(x, y)] = 1

    def place_toggle(self, x, y):
        pass


if __name__ == '__main__':
    game = GameWorld(5, 5)
    game.place_player(1, 2)
    game.place_object(1, 3)
    game.place_object(3, 2)

    print(game)
