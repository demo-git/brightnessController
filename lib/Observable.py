# coding: utf-8


class Observable:
    __observers = None

    def __init__(self):
        self.__observers = []

    # add one observer
    def add_observer(self, observer):
        self.__observers.append(observer)

    # add list of observers
    def add_observers(self, observers):
        self.__observers = observers

    # notify all observers
    def notify(self, args):
        for observer in self.__observers:
            observer.update(args)
