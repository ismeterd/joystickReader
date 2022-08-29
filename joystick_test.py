import pygame
from joystick import Joystick


class InputTest:
    def __init__(self):
        pygame.init()
        self.joycount = pygame.joystick.get_count()
        self.joys = []

    def initialize(self):
        if self.joycount == 0:
            print("\nNo joysticks were detected!")
            # to be exited the program with code 1.
        else:
            print(f"\nDetected {self.joycount} joystick/joysticks")
            for i in range(self.joycount):
                self.joys.append(Joystick(i))


if __name__ == "__main__":
    program = InputTest()
    program.initialize()
