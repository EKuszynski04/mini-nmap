from dataclasses import dataclass
from models import PortState

@dataclass
class ScanResult:
    port: int
    state: PortState
    service: str = ''
    error_msg: str = ''
    
