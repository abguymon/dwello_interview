from __future__ import annotations
from exceptions import NameAlreadyExistsException, NameNotFoundException
from device import Device
from typing import List

class Hub:
    def __init__(self, name: str):
        self.name = name
        self.devices = {}
        return
    
    def pair_device(self, device: Device) -> bool:
        if device.get_name() in self.devices:
            raise NameAlreadyExistsException
        else:
            self.devices[device.get_name()] = device
            device.pair(self)
            return True

    def get_device_state(self, device_name: str) -> int:
        if device_name not in self.devices:
            raise NameNotFoundException
        else:
            return self.devices[device_name].get_info()

    def list_devices(self) -> List[Device]:
        return self.devices.keys
    
    def remove_device(self, device_name: str) -> bool:
        if device_name not in self.devices:
            raise NameNotFoundException
        else:
            self.devices[device_name].unpair()
            del self.devices[device_name]
            return True