# coding: utf-8
from abc import ABCMeta, abstractmethod


class Observer:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, args):
        pass
