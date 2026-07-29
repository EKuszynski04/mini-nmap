from dataclasses import dataclass
from models import PortState

# A class structure that stores the result of the scans.
@dataclass
class ScanResult:
    # Port that was scanned
    port: int
    # The state of the port e.g. Open/Timeout
    state: PortState
    # Which service the scanned port represents e.g. port 22 = ssh
    service: str = ''
    #  Error message accompying any result other than open
    error_msg: str = ''
    
