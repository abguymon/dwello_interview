from dwelling import Dwelling
from hub import Hub
from device import Device, Switch, Dimmer, Lock, Thermostat
from exceptions import *
from typing import List


dwellings = {}
hubs = {}
devices = {}


def create_dwelling(name: str) -> Dwelling:
    if name is None:
        raise NameRequiredException
    elif name in dwellings:
        raise NameAlreadyExistsException
    else:
        dwelling = Dwelling(name)
        dwellings[name] = Dwelling
        return dwelling

def list_dwellings() -> List[str]:
    return dwellings.keys()

def get_dwelling(name: str) -> Dwelling:
    if name not in dwellings:
        raise NameNotFoundException
    else:
        return dwellings[name]

def delete_dwelling(name: str) -> bool:
    if name not in dwellings:
        raise NameNotFoundException
    else:
        del dwellings[name]
        return True

def create_hub(name: str) -> Hub:
    if name is None:
        raise NameRequiredException
    elif name in hubs:
        raise NameAlreadyExistsException
    else:
        hub = Hub(name)
        hubs[name] = hub
        return hub

def list_hubs() -> List[str]:
    return hubs.keys()

def get_hub(name: str) -> Hub:
    if name not in hubs:
        raise NameNotFoundException
    else:
        return hubs[name]

def delete_hub(name: str) -> bool: 
    if name not in hubs:
        raise NameNotFoundException
    else:
        del hubs[name]
        return True

def create_device(name:str, type:str)-> Device:
    if name is None:
        raise NameRequiredException
    elif name in devices:
        raise NameAlreadyExistsException
    else:
        if type == 'switch':
            switch = Switch(name)
            devices[name] = switch
            return switch
        elif type == 'dimmer':
            dimmer = Dimmer(name)
            devices[name] = dimmer
            return dimmer
        elif type == 'lock':
            lock = Lock(name)
            devices[name] = lock
            return lock
        elif type == 'thermostat':
            thermostat = Thermostat(name)
            devices[name] = thermostat
            return thermostat
        else:
            raise DeviceTypeNotExistException

def list_devices()-> List[str]:
    return devices.keys()

def get_device(name:str)-> Device:
    if name not in devices:
        raise NameNotFoundException
    else:
        return devices[name]

def delete_device(name:str):
    if name not in devices:
        raise NameNotFoundException
    elif devices[name].is_paired():
        raise DeviceCannotBeDeletedException
    else:
        del devices[name]
        return

    