
class NameAlreadyExistsException(Exception):
    def __init__(self, message="Name already exists, please try another name"):
        super().__init__(message)

class NameRequiredException(Exception):
    def __init__(self, message="Name required, please enter a name"):
        super().__init__(message)

class NameNotFoundException(Exception):
    def __init__(self, message="Name entered cannot be found"):
        super().__init__(message)

class DeviceCannotBeDeletedException(Exception):
    def __init__(self, message="Device is currently paired to a hub, please unpair before deleting"):
        super().__init__(message)

class StateOutOfRangeException(Exception):
    def __init__(self, message="Desired state falls outside range"):
        super().__init__(message)

class IncorrectCombinationException(Exception):
    def __init__(self, message="Entered combination does not match saved combination"):
        super().__init__(message)

class DeviceTypeNotExistException(Exception):
    def __init__(self, message="Entered device type does not exist"):
        super().__init__(message)