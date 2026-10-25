from enum import Enum

# A class enum that stores various states the port can be in after scans.
class PortState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    OPEN_FILTERED = "open|filtered"
    TIMEOUT = "timeout"
    ERROR = "error"

  