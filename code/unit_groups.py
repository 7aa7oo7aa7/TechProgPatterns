import units
from abc import ABC, abstractmethod


#==============================================================================================================
# abstract Ultra Unit classes


class UltraUnit(units.Unit):
    """Abstract class for ultraunit"""
    def __init__(self, *args):
        self.unit_num = 5
        self.children = args
        super().__init__({ 
                        'damage': self.children[0].characteristics['damage'] * self.unit_num, 
                        'defense': self.children[0].characteristics['defense'] * self.unit_num, 
                        'speed': self.children[0].characteristics['speed'], 
                        'range': self.children[0].characteristics['range']
                        })
    
    def execute(self):  # will be redone in part 3, when there will be actions
        for child in self.children:
            child.execute() 
    
    def ability(self):
        pass


#==============================================================================================================
# concrete Ultra Unit classes

# Faction 1 ultra unit classes


class Faction1UltraUnit1(UltraUnit):
    """Class for ultraunit 1 of faction 1"""
    def __init__(self, *args):
        super().__init__(*args)
        self.characteristics['name'] = 'Ultraunit 1'
        self.characteristics['faction'] = 1


class Faction1UltraUnit2(UltraUnit):
    """Class for ultraunit 2 of faction 1"""
    def __init__(self, *args):
        super().__init__(*args)
        self.characteristics['name'] = 'Ultraunit 2'
        self.characteristics['faction'] = 1


class Faction1UltraUnit3(UltraUnit):
    """Class for ultraunit 3 of faction 1"""
    def __init__(self, *args):
        super().__init__(*args)
        self.characteristics['name'] = 'Ultraunit 3'
        self.characteristics['faction'] = 1


# Faction 2 ultra unit classes


class Faction2UltraUnit1(UltraUnit):
    """Class for ultraunit 1 of faction 2"""
    def __init__(self, *args):
        super().__init__(*args)
        self.characteristics['name'] = 'Ultraunit 1'
        self.characteristics['faction'] = 2


class Faction2UltraUnit2(UltraUnit):
    """Class for ultraunit 2 of faction 2"""
    def __init__(self, *args):
        super().__init__(*args)
        self.characteristics['name'] = 'Ultraunit 2'
        self.characteristics['faction'] = 2


class Faction2UltraUnit3(UltraUnit):
    """Class for ultraunit 3 of faction 2"""
    def __init__(self, *args):
        super().__init__(*args)
        self.characteristics['name'] = 'Ultraunit 3'
        self.characteristics['faction'] = 2


#==============================================================================================================
# Super Unit classes, decorator and adapter

def SuperUnitDecorator(func):
    def wrapped():
        pass
    return wrapped


class UnitGroupAdapter(ABC):
    """Adapter class between SuperUnit and UltraUnit"""
    def __init__(self, *args):
        self.children = args
    
    def execute(self, child):
        pass


class SuperUnit(units.Unit):
    """Abstract class for superunit"""
    def __init__(self, *args):
        self.children = args
        super().__init__({
                        'name': 'Superunit', 
                        'damage': sum(self.children[i].characteristics['damage'] for i in range(3)), 
                        'defense': sum(self.children[i].characteristics['defense'] for i in range(3)), 
                        'speed': min(self.children[i].characteristics['speed'] for i in range(3)), 
                        'range': min(self.children[i].characteristics['range'] for i in range(3))
                        })
        self.adapter = UnitGroupAdapter()
    
    @SuperUnitDecorator
    def execute(self):
        for child in self.children:
            self.adapter.execute(child)  # will be redone in part 3, this one is pattern demonstration
    
    def ability(self):
        pass


class Faction1SuperUnit(SuperUnit):
    """Class for superunit of faction 1"""
    def __init__(self, *args):
        super().__init__(*args)
        self.characteristics['faction'] = 1


class Faction2SuperUnit(SuperUnit):
    """Class for superunit of faction 2"""
    def __init__(self, *args):
        super().__init__(*args)
        self.characteristics['faction'] = 2
