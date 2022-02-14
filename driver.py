from api import *

# CREATING DWELLINGS
dwelling_a = create_dwelling("Adam's Apartments")
dwelling_b = create_dwelling("Ben's Apartments")

# LISTING ALL DWELLINGS
print(list_dwellings())

# ADDING A RESIDENT
dwelling_a.add_resident("John")
print(dwelling_a.residents)

# REMOVING A RESIDENT
dwelling_a.vacant("John")
print(dwelling_a.residents)

# CREATING A HUB
hub_a = create_hub("Adam's Hub")
print(list_hubs())

# INSTALLING A HUB
dwelling_a.install_hub(hub_a)

# CREATING A DEVICE
thermostat_a = create_device("Adam's Thermostat", "thermostat")
print(list_devices())

# PAIR DEVICE
hub_a.pair_device(thermostat_a)

# LIST DEVICES
hub_a.list_devices()

# GET DEVICE STATE
print(hub_a.get_device_state("Adam's Thermostat"))

# REMOVE DEVICE
hub_a.remove_device("Adam's Thermostat")

# MODIFY DEVICE
thermostat_a = get_device("Adam's Thermostat")
thermostat_a.modify(72)

# DEVICE INFO
print(thermostat_a.get_info())

# LIST ALL DEVICES
print(list_devices())

# DELETE DEVICE
delete_device("Adam's Thermostat")


######### SOME EXAMPLE TESTS

# DUPLICATE DWELLING NAMES
try:
    create_dwelling("Adam's Apartments")
except NameAlreadyExistsException as ex:
    print(ex)

# DELETE PAIRED DEVICE
try:
    lock_a = create_device("Paired Lock", "lock")
    hub_a.pair_device(lock_a)
    delete_device("Paired Lock")
except DeviceCannotBeDeletedException as ex:
    print(ex)

# SET DIMMER TO GREATER THAN 100
try:
    dimmer_a = create_device("Good Dimmer", "dimmer")
    dimmer_a.modify(200)
except StateOutOfRangeException as ex:
    print(ex)