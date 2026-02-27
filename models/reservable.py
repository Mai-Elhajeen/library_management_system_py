from abc import ABC, abstractmethod

# This class defines the Reservable interface, which can be implemented by any library item that can be reserved.
class Reservable(ABC):
    @abstractmethod
    def reserve(self, user):
        pass