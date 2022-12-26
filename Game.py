import pygame
import math
import Conways

class Game:
    def __init__(self, params):
        self.square_size = 30

        self.nb_carres_x = 0
        if params["nb_carres_x"] == 0:
            self.nb_carres_x = math.floor(pygame.display.Info().current_w / self.square_size)
        else:
            self.nb_carres_x = params["nb_carres_x"]

        self.nb_carres_y = 0
        if params["nb_carres_y"] == 0:
            self.nb_carres_y = math.floor(pygame.display.Info().current_h / self.square_size)
        else:
            self.nb_carres_y = params["nb_carres_y"]

        self.width = self.nb_carres_x * self.square_size
        self.height = self.nb_carres_y * self.square_size

        self.window = pygame.display.set_mode((self.width, self.height))
        self.bg_color = (255, 255, 255)
        self.wait_time = 20
        self.time_between_frames = params["attente"]

        self.conway = Conways.Conways(self.width, self.height, self.square_size)

    def get_w(self):
        return self.width

    def get_h(self):
        return self.height

    def get_window(self):
        return self.window

    def main_loop(self):
        play = True
        edit_mode = False
        last_frame = 0

        while(play):

            # traiter les évènements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        edit_mode = True
                        mod = -1
                        print("entering edit mode. Press <escape> to quit.")
                    if event.key == pygame.K_ESCAPE:
                        edit_mode = False
                        print("quiting edit mode.")
                if edit_mode:
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        mouse_pos = pygame.mouse.get_pos()
                        mod = self.conway.God(mouse_pos, mod) # invert cell state
                    else:
                        mod = -1

            # afficher la grille
            self.window.fill(self.bg_color)
            self.conway.print(self.window)
            pygame.display.update()
            pygame.time.wait(self.wait_time)

            # faire évoluer le jeu
            if not edit_mode\
               and last_frame + self.time_between_frames < pygame.time.get_ticks():
                self.conway.tour_de_jeu()
                last_frame = pygame.time.get_ticks()

