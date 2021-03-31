import unit_factory
from abc import ABC, abstractmethod


#==============================================================================================================
# Abstract base class


class Base(ABC):
    """Abstract class for player/enemy base"""
    def __init__(self, defense, player_gold):
        self.defense = defense
        self.player_gold = player_gold
        self.factory = dict()
        self.improvement_options = dict()
    
    @abstractmethod
    def create_unit(self, unit_id, *args):
        pass

    @abstractmethod
    def improvement(self, improvement_id):
        pass


#==============================================================================================================
# Concrete base classes


class Faction1Base(Base):
    """Class for faction 1 base"""
    def __init__(self):
        super().__init__(400, 50)
        self.factory = {
                        "Unit 1": unit_factory.Faction1Unit1Factory(), 
                        "Unit 2": unit_factory.Faction1Unit2Factory(), 
                        "Unit 3": unit_factory.Faction1Unit3Factory(),
                        "Unique Unit": unit_factory.Faction1UniqueUnitFactory()
                        }
        self.improvement_options = {
                                    "Improvement 1": 100, 
                                    "Improvement 2": 100, 
                                    "Improvement 3": 100, 
                                    "Improvement 4": 200, 
                                    "Improvement 5": 200
                                    }

    def create_unit(self, unit_id, *args):
        if self.player_gold < self.factory[unit_id].cost:
            return None
        unit = self.factory[unit_id].create(*args)
        return unit

    def improvement(self, improvement_id):
        if self.player_gold < self.improvement_options[improvement_id]:
                return False
        if improvement_id == "Improvement 1":
            pass
        elif improvement_id == "Improvement 2":
            pass
        elif improvement_id == "Improvement 3":
            pass
        elif improvement_id == "Improvement 4":
            pass
        elif improvement_id == "Improvement 5":
            pass
        return True


class Faction2Base(Base):
    """Class for faction 2 base"""
    def __init__(self):
        super().__init__(400, 50)
        self.factory = {
                        "Unit 1": unit_factory.Faction2Unit1Factory(), 
                        "Unit 2": unit_factory.Faction2Unit2Factory(), 
                        "Unit 3": unit_factory.Faction2Unit3Factory(),
                        "Unique Unit": unit_factory.Faction2UniqueUnitFactory()
                        }
        self.improvement_options = {
                                    "Improvement 1": 100, 
                                    "Improvement 2": 100, 
                                    "Improvement 3": 100, 
                                    "Improvement 4": 200, 
                                    "Improvement 5": 200
                                    }

    def create_unit(self, unit_id, *args):
        if self.player_gold < self.factory[unit_id].cost:
            return None
        unit = self.factory[unit_id].create(*args)
        return unit

    def improvement(self, improvement_id):
        if self.player_gold < self.improvement_options[improvement_id]:
                return False
        if improvement_id == "Improvement 1":
            pass
        elif improvement_id == "Improvement 2":
            pass
        elif improvement_id == "Improvement 3":
            pass
        elif improvement_id == "Improvement 4":
            pass
        elif improvement_id == "Improvement 5":
            pass
        return True
