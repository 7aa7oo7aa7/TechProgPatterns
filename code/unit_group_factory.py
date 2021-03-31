import unit_groups
import abstract_factory
from abc import ABC, abstractmethod


#==============================================================================================================
# Abstract factory class


class UnitGroupFactory(abstract_factory.AbstractFactory):
    """Abstract factory for ultra units"""
    def __init__(self):
        super().__init__(0)
    
    @abstractmethod
    def create(self, *args):
        pass
    
    def remove(self, unit):
        for child in unit.children:
            child.health = 0
        super().remove(unit)


#==============================================================================================================
# Faction 1 factory classes


class Faction1UltraUnit1Factory(UnitGroupFactory):
    """Factory for ultra unit 1 of faction 1"""
    def __init__(self):
        super().__init__()
    
    def create(self, *args):
        unit = unit_groups.Faction1UltraUnit1(*args)
        self.units_in_game.add(unit)
        return unit


class Faction1UltraUnit2Factory(UnitGroupFactory):
    """Factory for ultra unit 2 of faction 1"""
    def __init__(self):
        super().__init__()
    
    def create(self, *args):
        unit = unit_groups.Faction1UltraUnit2(*args)
        self.units_in_game.add(unit)
        return unit


class Faction1UltraUnit3Factory(UnitGroupFactory):
    """Factory for ultra unit 3 of faction 1"""
    def __init__(self):
        super().__init__()
    
    def create(self, *args):
        unit = unit_groups.Faction1UltraUnit3(*args)
        self.units_in_game.add(unit)
        return unit


class Faction1SuperUnitFactory(UnitGroupFactory):
    """Factory for super unit of faction 1"""
    def __init__(self):
        super().__init__()
    
    def create(self, *args):
        unit = unit_groups.Faction1SuperUnit(*args)
        self.units_in_game.add(unit)
        return unit


#==============================================================================================================
# Faction 2 factory classes


class Faction2UltraUnit1Factory(UnitGroupFactory):
    """Factory for ultra unit 1 of faction 2"""
    def __init__(self):
        super().__init__()
    
    def create(self, *args):
        unit = unit_groups.Faction2UltraUnit1(*args)
        self.units_in_game.add(unit)
        return unit


class Faction2UltraUnit2Factory(UnitGroupFactory):
    """Factory for ultra unit 2 of faction 2"""
    def __init__(self):
        super().__init__()
    
    def create(self, *args):
        unit = unit_groups.Faction2UltraUnit2(*args)
        self.units_in_game.add(unit)
        return unit


class Faction2UltraUnit3Factory(UnitGroupFactory):
    """Factory for ultra unit 3 of faction 2"""
    def __init__(self):
        super().__init__()
    
    def create(self, *args):
        unit = unit_groups.Faction2UltraUnit3(*args)
        self.units_in_game.add(unit)
        return unit


class Faction2SuperUnitFactory(UnitGroupFactory):
    """Factory for super unit of faction 2"""
    def __init__(self):
        super().__init__()
    
    def create(self, *args):
        unit = unit_groups.Faction2SuperUnit(*args)
        self.units_in_game.add(unit)
        return unit
