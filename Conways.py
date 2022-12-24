import pygame
import math
import copy
import random as rand

class Conways:
    def __init__(self, width, height, square_size):
        self.square_size = square_size
        self.nb_carres_x = math.floor(pygame.display.Info().current_w / self.square_size)
        self.nb_carres_y = math.floor(pygame.display.Info().current_h / self.square_size)
        self.square_color = (0, 0, 0)

        self.map = [[0 for i in range(self.nb_carres_x)] for j in range(self.nb_carres_y)]

    def print(self, window):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if self.map[x][y] == 1:
                    rect = pygame.Rect(
                        x * self.square_size + 1, y * self.square_size + 1,
                        self.square_size - 2, self.square_size - 2
                    )
                    pygame.draw.rect(window, self.square_color, rect)

    def tour_de_jeu(self):
        adjacents = [
            [-1, -1],
            [0 , -1],
            [1 , -1],
            [-1,  0],
            [1 ,  0],
            [-1,  1],
            [0 ,  1],
            [1 ,  1]
        ]

        old_grid = copy.deepcopy(self.map)

        for x in range(1, len(self.map) - 1, 1):
            for y in range(1, len(self.map[x]) - 1, 1):
                nb_vivants = 0
                for adj in adjacents:
                    if old_grid[x + adj[0]][y + adj[1]] == 1:
                        nb_vivants += 1

                if old_grid[x][y] == 1:
                    if nb_vivants < 2 or nb_vivants > 3:
                        self.map[x][y] = 0
                else:
                    if nb_vivants == 3:
                        self.map[x][y] = 1

