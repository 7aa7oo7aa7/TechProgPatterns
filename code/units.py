from abc import ABC, abstractmethod

#================================================================================================================================================================================================
# Abstract factory class

class AbstractFactory(ABC):
    """Abstract factory"""
    def __init__(self, cost):
        self.units_in_game = set()
        self.cost = cost
    
    @abstractmethod
    def create(self):
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

#==============================================================================================================
# Abstract unit classes

class Unit(ABC):
    """Abstract class for all units"""
    def __init__(self, characteristics):
        self.characteristics = characteristics
        self.health = self.characteristics['defense']


class UniqueUnit(Unit):
    """Abstract class for all unique units"""
    def __init__(self, characteristics):
        super().__init__(characteristics)


class Faction1Unit(Unit):
    """Abstract class for units of faction 1"""
    def __init__(self, characteristics):
        super().__init__(characteristics)
        self.characteristics['faction'] = 1


class Faction2Unit(Unit):
    """Abstract class for units of faction 2"""
    def __init__(self, characteristics):
        super().__init__(characteristics)
        self.characteristics['faction'] = 2

#==============================================================================================================
# Abstract base class

class Base(ABC):
    """Abstract class for player/enemy base"""
    def __init__(self, defense, player_gold):
        self.defense = defense
        self.player_gold = player_gold
    
    @abstractmethod
    def create_unit(self):
        pass

    @abstractmethod
    def improvement(self):
        pass

#================================================================================================================================================================================================
# Concrete unit classes

# Faction 1 unit classes

class Faction1Unit1(Faction1Unit):
    """Class for unit 1 of faction 1"""
    def __init__(self):
        super().__init__({'name': 'Unit 1', 'damage': 10, 'defense': 40, 'speed': 1, 'range': 1})



class Faction1Unit2(Faction1Unit):
    """Class for unit 2 of faction 1"""
    def __init__(self):
        super().__init__({'name': 'Unit 2', 'damage': 20, 'defense': 15, 'speed': 2, 'range': 10})



class Faction1Unit3(Faction1Unit):
    """Class for unit 3 of faction 1"""
    def __init__(self):
        super().__init__({'name': 'Unit 3', 'damage': 5, 'defense': 30, 'speed': 3, 'range': 2})

#==============================================================================================================
# Faction 2 unit classes

class Faction2Unit1(Faction2Unit):
    """Class for unit 1 of faction 2"""
    def __init__(self):
        super().__init__({'name': 'Unit 1', 'damage': 20, 'defense': 20, 'speed': 1, 'range': 1})



class Faction2Unit2(Faction2Unit):
    """Class for unit 2 of faction 2"""
    def __init__(self):
        super().__init__({'name': 'Unit 2', 'damage': 20, 'defense': 40, 'speed': 2, 'range': 4})



class Faction2Unit3(Faction2Unit):
    """Class for unit 3 of faction 2"""
    def __init__(self):
        super().__init__({'name': 'Unit 3', 'damage': 20, 'defense': 30, 'speed': 3, 'range': 1})

#==============================================================================================================
# Unique unit classes

class Faction1UniqueUnit(UniqueUnit):
    """Class for unique unit of faction 1"""
    def __init__(self):
        super().__init__({'name': 'Unique Unit', 'damage': 80, 'defense': 180, 'speed': 1, 'range': 10})


class Faction2UniqueUnit(UniqueUnit):
    """Class for unique unit of faction 2"""
    def __init__(self):
        super().__init__({'name': 'Unique Unit', 'damage': 90, 'defense': 200, 'speed': 3, 'range': 1})


#==============================================================================================================
# Concrete factory classes

# Faction 1 factory classes

class Faction1Unit1Factory(AbstractFactory):
    """Factory for unit 1 of faction 1"""
    def __init__(self):
        super().__init__(50)
    
    def create(self):
        unit = Faction1Unit1()
        self.units_in_game.add(unit)
        return unit


class Faction1Unit2Factory(AbstractFactory):
    """Factory for unit 2 of faction 1"""
    def __init__(self):
        super().__init__(75)
    
    def create(self):
        unit = Faction1Unit2() 
        self.units_in_game.add(unit)
        return unit


class Faction1Unit3Factory(AbstractFactory):
    """Factory for unit 3 of faction 1"""
    def __init__(self):
        super().__init__(100)
    
    def create(self):
        unit = Faction1Unit3() 
        self.units_in_game.add(unit)
        return unit


class Faction1UniqueUnitFactory(AbstractFactory):
    """Factory for unique unit of faction 1"""
    def __init__(self):
        super().__init__(500)

    def create(self):
        if len(self.units_in_game) == 0:
            unit = Faction1UniqueUnit()
            self.units_in_game.add(unit)
            return unit
        return None

    def remove(self):
        self.units_in_game = set()

#==============================================================================================================
# Faction 2 factory classes

class Faction2Unit1Factory(AbstractFactory):
    """Factory for unit 1 of faction 2"""
    def __init__(self):
        super().__init__(50)
    
    def create(self):
        unit = Faction2Unit1() 
        self.units_in_game.add(unit)
        return unit


class Faction2Unit2Factory(AbstractFactory):
    """Factory for unit 2 of faction 2"""
    def __init__(self):
        super().__init__(75)
    
    def create(self):
        unit = Faction2Unit2() 
        self.units_in_game.add(unit)
        return unit


class Faction2Unit3Factory(AbstractFactory):
    """Factory for unit 3 of faction 2"""
    def __init__(self):
        super().__init__(100)
    
    def create(self):
        unit = Faction2Unit3() 
        self.units_in_game.add(unit)
        return unit


class Faction2UniqueUnitFactory(AbstractFactory):
    """Factory for unique unit of faction 1"""
    def __init__(self):
        super().__init__(500)

    def create(self):
        if len(self.units_in_game) == 0:
            unit = Faction1UniqueUnit() 
            self.units_in_game.add(unit)
            return unit
        return None

    def remove(self):
        self.units_in_game = set()

#==============================================================================================================
# Concrete base classes

class Faction1Base(Base):
    """Class for faction 1 base"""
    def __init__(self):
        super().__init__(400, 50)
        self.factory = {"Unit 1": Faction1Unit1Factory(), 
        "Unit 2": Faction1Unit2Factory(), 
        "Unit 3": Faction1Unit3Factory(),
        "Unique Unit": Faction1UniqueUnitFactory()}
        self.improvement_options = {"Improvement 1", "Improvement 2", "Improvement 3", "Improvement 4", "Improvement 5"}

    def create_unit(self, unit_id):
        if self.player_gold < self.factory[unit_id].cost:
            return None
        unit = self.factory[unit_id].create()
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
        self.factory = {"Unit 1": Faction2Unit1Factory(), 
        "Unit 2": Faction2Unit2Factory(), 
        "Unit 3": Faction2Unit3Factory(),
        "Unique Unit": Faction2UniqueUnitFactory()}
        self.improvement_options = {"Improvement 1": 100, "Improvement 2": 100, "Improvement 3": 100, "Improvement 4": 200, "Improvement 5": 200}

    def create_unit(self, unit_id):
        if self.player_gold < self.factory[unit_id].cost:
            return None
        unit = self.factory[unit_id].create()
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

#=================================================================================================================================================================================================================
# Interface

class MainInterface(object):
    """Main interface that appears when you start the game"""
    def __init__(self):
        self.factions = {'faction 1', 'faction 2'}

    def choose_faction(self):
        print(f"Choose your faction from {self.factions}: ")
        player_faction = input()
        if player_faction not in self.factions:
            print(f"Error: faction {player_faction} does not exist.")
            return False
        if player_faction == 'faction 1':
            player_base = Faction1Base()
        elif player_faction == 'faction 2':
            player_base = Faction2Base()
        self.base_interface = BaseInterface(player_base)


class BaseInterface(object):
    """Class for base interface"""
    def __init__(self, base):
        self.base = base
        self.options = {'create unit', 'improvement', 'balance'}
        self.units = []

    def basic_interface(self):
        while True:
            print(f"You are in your base. Choose one from {self.options}: ")
            option = input()
            if option in self.options:
                if option == 'create unit':
                    self.create_unit()
                elif option == 'improvement':
                    self.improvement()
                elif option == 'balance':
                    print(self.base.player_gold)
            else:
                print("Error: you cannot perform this command.")

    def create_unit(self):
        print("Enter unit id from {}: ".format(self.base.factory.keys()))
        unit_id = input()
        if unit_id in self.base.factory.keys():
            unit = self.base.create_unit(unit_id)
            if unit == None:
                print(f"You do not have enough gold to create {unit_id}.")
            else:
                print(f"{unit_id} is created.")
                unit_interface = UnitInterface(unit)
                self.units.insert(unit_interface)
        else:
            print("Error: unit with this id does not exist.")

    def improvement(self):
        print("Enter improvement id from {}: ".format(self.base.improvement_options))
        improvement_id = input()
        if improvement_id in self.base.improvement_options:
            result = self.base.improvement(improvement_id)
            if not result:
                print(f"You do not have enough gold to make {improvement_id}.")
            else:
                print(f"{improvement_id} is created.")
        else:
            print("Error: improvement with this id does not exist.")


class UnitInterface(object):
    def __init__(self, unit):
        self.unit = unit

    def basic_interface(self):
        print(f"You are now controlling {self.unit.characteristics['name']}. Your current health is {self.unit.health}")

    def info(self):
        print(self.unit.characteristics)


def main():
    pass

