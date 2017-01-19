# coding: utf-8


class Observable:
    _observers = None

    def __init__(self):
        self._observers = []

    # add one observer
    def add_observer(self, observer):
        self._observers.append(observer)

    # add list of observers
    def add_observers(self, observers):
        self._observers = observers

    # notify all observers
    def notify(self, args):
        for observer in self._observers:
            observer.update(args)
