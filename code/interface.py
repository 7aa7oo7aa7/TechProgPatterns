from abc import ABC, abstractmethod
import base


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
            player_base = base.Faction1Base()
        elif player_faction == 'faction 2':
            player_base = base.Faction2Base()
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
        print(f"Enter improvement id from {self.base.improvement_options}: ")
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
