from abc import ABC, abstractmethod


#================================================================================================================================================================================================
# Abstract factory class


class AbstractFactory(ABC):
    """Abstract factory"""
    def __init__(self, cost):
        self.units_in_game = set()
        self.cost = cost
    
    @abstractmethod
    def create(self, *args):
        """Creates new instance of unit"""
        pass

    def remove(self, unit):
        """Removes an instance of unit"""
        self.units_in_game.remove(unit)
    
    def syncronize(self):
        """collect information about number of units, remove dead ones"""
        for unit in self.units_in_game:
            if unit.health <= 0:
                self.remove(unit)
