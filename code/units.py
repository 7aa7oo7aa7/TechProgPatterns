from abc import ABC, abstractmethod


#==============================================================================================================
# Abstract unit classes


class Unit(ABC):
    """Abstract class for all units"""
    def __init__(self, characteristics):
        self.characteristics = characteristics
        self.health = self.characteristics['defense']
    
    @abstractmethod
    def ability(self):
        pass


class UniqueUnit(Unit):
    """Abstract class for all unique units"""
    def __init__(self, characteristics):
        super().__init__(characteristics)
    
    @abstractmethod
    def ability(self):
        pass


class Faction1Unit(Unit):
    """Abstract class for units of faction 1"""
    def __init__(self, characteristics):
        super().__init__(characteristics)
        self.characteristics['faction'] = 1
    
    @abstractmethod
    def ability(self):
        pass


class Faction2Unit(Unit):
    """Abstract class for units of faction 2"""
    def __init__(self, characteristics):
        super().__init__(characteristics)
        self.characteristics['faction'] = 2
    
    @abstractmethod
    def ability(self):
        pass


#================================================================================================================================================================================================
# Concrete unit classes

# Faction 1 unit classes


class Faction1Unit1(Faction1Unit):
    """Class for unit 1 of faction 1"""
    def __init__(self):
        super().__init__({
                        'name': 'Unit 1', 
                        'damage': 10, 
                        'defense': 40, 
                        'speed': 1, 
                        'range': 1
                        })

    def ability(self):
        pass


class Faction1Unit2(Faction1Unit):
    """Class for unit 2 of faction 1"""
    def __init__(self):
        super().__init__({
                        'name': 'Unit 2', 
                        'damage': 20, 
                        'defense': 15, 
                        'speed': 2, 
                        'range': 10
                        })

    def ability(self):
        pass


class Faction1Unit3(Faction1Unit):
    """Class for unit 3 of faction 1"""
    def __init__(self):
        super().__init__({
                        'name': 'Unit 3', 
                        'damage': 5, 
                        'defense': 30, 
                        'speed': 3, 
                        'range': 2
                        })
    
    def ability(self):
        pass


#==============================================================================================================
# Faction 2 unit classes


class Faction2Unit1(Faction2Unit):
    """Class for unit 1 of faction 2"""
    def __init__(self):
        super().__init__({
                        'name': 'Unit 1', 
                        'damage': 20, 
                        'defense': 20, 
                        'speed': 1, 
                        'range': 1
                        })

    def ability(self):
        pass


class Faction2Unit2(Faction2Unit):
    """Class for unit 2 of faction 2"""
    def __init__(self):
        super().__init__({
                        'name': 'Unit 2', 
                        'damage': 20, 
                        'defense': 40, 
                        'speed': 2, 
                        'range': 4
                        })

    def ability(self):
        pass


class Faction2Unit3(Faction2Unit):
    """Class for unit 3 of faction 2"""
    def __init__(self):
        super().__init__({
                        'name': 'Unit 3', 
                        'damage': 20, 
                        'defense': 30, 
                        'speed': 3, 
                        'range': 1
                        })

    def ability(self):
        pass


#==============================================================================================================
# Unique unit classes

class Faction1UniqueUnit(UniqueUnit):
    """Class for unique unit of faction 1"""
    def __init__(self):
        super().__init__({
                        'name': 'Unique Unit', 
                        'damage': 80, 
                        'defense': 180, 
                        'speed': 1, 
                        'range': 10
                        })
    
    def ability(self):
        pass


class Faction2UniqueUnit(UniqueUnit):
    """Class for unique unit of faction 2"""
    def __init__(self):
        super().__init__({
                        'name': 'Unique Unit', 
                        'damage': 90, 
                        'defense': 200, 
                        'speed': 3, 
                        'range': 1
                        })
    
    def ability(self):
        pass
