from dataclasses import dataclass
from models.scan_type import ScanType
import ipaddress

# A class structure that stores the configuration data of the scans.

@dataclass
class ScanConfig:
    ip: str 
    ports: list[int]
    timeout: float
    scan_type: ScanType