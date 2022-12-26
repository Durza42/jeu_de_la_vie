import pygame
import Game
import accueil

def main():
    params = {
        "nb_carres_x" : 0,
        "nb_carres_y" : 0,
        "attente" : 300,
        "continue" : False
    }

    accueil.menu(params)

    if params["continue"]:
        pygame.init()
        game = Game.Game(params)
        game.main_loop()

main()
