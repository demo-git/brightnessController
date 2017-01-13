# coding: utf-8


class Observable:
    __observers = None

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notify(self, args):
        for observer in self.__observers:
            observer.update(args)
