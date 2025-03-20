from enum import Enum
from abc import ABC, abstractmethod
import random

# Fix the enum class
class ConnectionState(Enum):
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"

class IDevice(ABC):
    
    @abstractmethod
    def connect(self) -> bool:
        # Should randomly send True or False
        return random.choice([True, False])
    
    @abstractmethod
    def disconnect(self) -> bool:
        # Should randomly send True or False
        return random.choice([True, False])
    
    @abstractmethod
    def get_serial_number(self) -> str:
        pass
    
    @abstractmethod
    def get_status(self) -> ConnectionState:
        pass
