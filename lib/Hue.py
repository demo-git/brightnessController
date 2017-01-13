# coding: utf-8


class Hue:
    __connect = None

    def __init__(self, connect):
        self.__connect = connect

    def change_state(self, on, intensity=None):
        # TODO: use api hue
        if on == 1:
            pass
        else:
            pass

    def update(self, intensity):
        if intensity > 0:
            self.change_state(1, intensity)
        else:
            self.change_state(0)
