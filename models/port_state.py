from enum import Enum

class PortState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    TIMEOUT = "timeout"
    ERROR = "error"