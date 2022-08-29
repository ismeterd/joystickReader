import pygame


class InputTest:
    def __init__(self):
        pygame.init()
        self.joycount = pygame.joystick.get_count()
        self.joys = []

