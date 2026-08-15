# File used to map different values forr enums.

from models.scan_type import ScanType

# Valid Scan Types Map
VALID_SCAN_TYPES_MAP = {"T": ScanType.TCP, "TCP": ScanType.TCP, "U":ScanType.UDP, "UDP":ScanType.UDP}