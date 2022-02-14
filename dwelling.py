from typing import List
from hub import Hub

class Dwelling:
    def __init__(self, name:str):
        self.name = name
        self.residents = []
        self.hub = None

    def add_resident(self, resident_name: str) -> bool:
        self.residents.append(resident_name)
        return True

    def vacant(self, resident_name:str) -> bool:
        if resident_name not in self.residents:
            print(f"{resident_name} cannot be found in dwelling")
            return False
        else:
            self.residents.remove(resident_name)
            return True
    
    def install_hub(self, hub: Hub) -> bool:
        if self.hub is None:
            self.hub = hub
            return True
        else:
            print("Dwelling already has hub, remove current hub before trying to install a new one.")
            return False
    