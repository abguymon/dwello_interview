from __future__ import annotations
from abc import ABC, abstractmethod

from exceptions import StateOutOfRangeException, IncorrectCombinationException
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hub import Hub


class Device(ABC):
    def __init__(self, name: str):
        self.name = name
        self.state = None
        self.hub = None
        return

    def get_info(self):
        return self.state

    @abstractmethod
    def modify(self):
        return

    def is_paired(self):
        if self.hub is None:
            return False
        else:
            return True
    
    def pair(self, hub: Hub):
        self.hub = hub
    
    def unpair(self):
        self.hub = None
    
    def get_name(self):
        return self.name

class Switch(Device):
    # Assume 0 is off 1 is on
    def __init__(self, name: str):
        super().__init__(name)
        self.state = 0
        return
    
    def modify(self):
        self.state = 1 - self.state
        return self.state

class Dimmer(Device):
    # Assume 0 is off 100 is full brightness
    def __init__(self, name: str):
        super().__init__(name)
        self.state = 0
        return

    def modify(self, new_state: int):
        if 0 > new_state or new_state > 100:
            raise StateOutOfRangeException
        else:
            self.state = new_state
            return

class Lock(Device):
    # Assume 0 is unlucked 1 is locked
    def __init__(self, name: str):
        super().__init__(name)
        self.combination = "0000"
        self.state = 0
        return

    def modify(self, combination: str):
        if combination == self.combination:
            self.state = 1 - self.state
            return self.state
        else:
            raise IncorrectCombinationException
    
    def change_combination(self, old_combination: str, new_combination:str):
        if old_combination == self.combination:
            self.change_combination = new_combination
        else:
            raise IncorrectCombinationException

class Thermostat(Device):
    def __init__(self, name: str):
        super().__init__(name)
        self.state = 68
        return

    def modify(self, new_state: int):
        if 40 > new_state or new_state > 100:
            raise StateOutOfRangeException
        else:
            self.state = new_state
            return True