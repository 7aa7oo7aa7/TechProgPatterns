import units
import abstract_factory
from abc import ABC, abstractmethod


# Faction 1 factory classes


class Faction1Unit1Factory(abstract_factory.AbstractFactory):
    """Factory for unit 1 of faction 1"""
    def __init__(self):
        super().__init__(50)
    
    def create(self):
        unit = units.Faction1Unit1()
        self.units_in_game.add(unit)
        return unit


class Faction1Unit2Factory(abstract_factory.AbstractFactory):
    """Factory for unit 2 of faction 1"""
    def __init__(self):
        super().__init__(75)
    
    def create(self):
        unit = units.Faction1Unit2() 
        self.units_in_game.add(unit)
        return unit


class Faction1Unit3Factory(abstract_factory.AbstractFactory):
    """Factory for unit 3 of faction 1"""
    def __init__(self):
        super().__init__(100)
    
    def create(self):
        unit = units.Faction1Unit3() 
        self.units_in_game.add(unit)
        return unit


class Faction1UniqueUnitFactory(abstract_factory.AbstractFactory):
    """Factory for unique unit of faction 1"""
    def __init__(self):
        super().__init__(500)

    def create(self):
        if len(self.units_in_game) == 0:
            unit = units.Faction1UniqueUnit()
            self.units_in_game.add(unit)
            return unit
        return None

    def remove(self):
        self.units_in_game = set()


#==============================================================================================================
# Faction 2 factory classes


class Faction2Unit1Factory(abstract_factory.AbstractFactory):
    """Factory for unit 1 of faction 2"""
    def __init__(self):
        super().__init__(50)
    
    def create(self):
        unit = units.Faction2Unit1() 
        self.units_in_game.add(unit)
        return unit


class Faction2Unit2Factory(abstract_factory.AbstractFactory):
    """Factory for unit 2 of faction 2"""
    def __init__(self):
        super().__init__(75)
    
    def create(self):
        unit = units.Faction2Unit2() 
        self.units_in_game.add(unit)
        return unit


class Faction2Unit3Factory(abstract_factory.AbstractFactory):
    """Factory for unit 3 of faction 2"""
    def __init__(self):
        super().__init__(100)
    
    def create(self):
        unit = units.Faction2Unit3() 
        self.units_in_game.add(unit)
        return unit


class Faction2UniqueUnitFactory(abstract_factory.AbstractFactory):
    """Factory for unique unit of faction 1"""
    def __init__(self):
        super().__init__(500)

    def create(self):
        if len(self.units_in_game) == 0:
            unit = units.Faction1UniqueUnit() 
            self.units_in_game.add(unit)
            return unit
        return None

    def remove(self):
        self.units_in_game = set()
