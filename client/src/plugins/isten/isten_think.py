from abc import abstractmethod, ABCMeta


class Think(metaclass=ABCMeta):
    @abstractmethod
    def think(self):
        pass


class Id(metaclass=ABCMeta):
    @abstractmethod
    def id(self):
        pass


class Ego(metaclass=ABCMeta):
    @abstractmethod
    def ego(self):
        pass


class SuperEgo(metaclass=ABCMeta):
    @abstractmethod
    def super_ego(self):
        pass


