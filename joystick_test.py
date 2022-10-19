import sys

import pygame
from joystick import Joystick


class InputTest:
    def __init__(self):
        pygame.init()
        self.joycount = pygame.joystick.get_count()
        self.joys = []
        self.event_joy = 0

        if self.joycount == 0:
            print("\nNo joysticks were detected!")
            # to be exited the program with code 1.
            self.quit(1)
        else:
            print(f"\nDetected {self.joycount} joystick/joysticks")
            for i in range(self.joycount):
                self.joys.append(Joystick(i))

    def run(self):
        while True:
            for event in [pygame.event.wait(), ] + pygame.event.get():
                event_name = pygame.event.event_name(event.type)
                event_joy = event.__dict__.get('joy')

                if event_name == "JoyDeviceAdded" or event_name == "AudioDeviceAdded":
                    pass
                else:
                    joystick_name = self.joys[self.event_joy].name
                    print(f"Joystick Name: {joystick_name}")

                # print(f"{event} -> {event_name} -> joy: {event_joy}")

                if event_name == "JoyAxisMotion" or event_name == "JoyHatMotion" or event_name == "JoyButtonDown" or event_name == "JoyButtonUp":
                    if event_name == "JoyAxisMotion":
                        event_axis = event.__dict__.get('axis')
                        event_value = event.__dict__.get('value')
                        self.joys[event_joy].axis[event_axis] = event_value

                    elif event_name == "JoyHatMotion":
                        event_value = event.__dict__.get('value')
                        event_hat = event.__dict__.get('hat')
                        self.joys[event_joy].hat[event_hat] = event_value

                    elif event_name == "JoyButtonDown":
                        event_buton = event.__dict__.get('button')
                        self.joys[event_joy].button[event_buton] = 1

                    elif event_name == "JoyButtonUp":
                        event_buton = event.__dict__.get('button')
                        self.joys[event_joy].button[event_buton] = 0

                    self.view_joystick_states(event_joy)

    def view_joystick_states(self, id):
        print(f"axis: {self.joys[id].axis}")
        print(f"hats: {self.joys[id].hat}")
        print(f"buttons: {self.joys[id].button}")
        print("----------------------------------------------")

    def quit(self, status=0):
        print("Program is ending...")
        pygame.quit()
        sys.exit(status)


if __name__ == "__main__":
    program = InputTest()
    program.run()
