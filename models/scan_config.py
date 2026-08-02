from dataclasses import dataclass
from models import PortState

# A class structure that stores the configuration data of the scans.
class ScanConfig:
    ip: str
    ports: list[int]
    timeout: float
    scan_type: str