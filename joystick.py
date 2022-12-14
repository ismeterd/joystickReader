import pygame


class Joystick:
    def __init__(self, id: int):
        self.id = id
        self.joy = pygame.joystick.Joystick(id)
        self.name = self.joy.get_name()
        self.joy.init()
        self.numeaxes = self.joy.get_numaxes()
        self.numballs = self.joy.get_numballs()
        self.numbuttons = self.joy.get_numbuttons()
        self.numhats = self.joy.get_numhats()

        self.axis = []
        for i in range(self.numeaxes):
            self.axis.append(self.joy.get_axis(i))

        self.ball = []
        for i in range(self.numballs):
            self.ball.append(self.joy.get_ball(i))

        self.button = []
        for i in range(self.numbuttons):
            self.button.append(self.joy.get_button(i))

        self.hat = []
        for i in range(self.numhats):
            self.hat.append(self.joy.get_hat(i))

    def view_joystick_details(self):
        print("\n----Joystick Details----")
        print(f"Joystick id : {self.id}")
        print(f"Joystick name: {self.name}")
        print()
        print(f"number of axis -> {self.numeaxes}")
        print(f"number of ball -> {self.numballs}")
        print(f"number of button -> {self.numbuttons}")
        print(f"number of hats -> {self.numhats}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    pass
