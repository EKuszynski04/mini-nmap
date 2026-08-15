# Parses.py responsible for parsing different inputs to match 
# different functions datatypes for validations

from utils.mappings import VALID_SCAN_TYPES_MAP
from utils.constants import ERROR_SCANTYPE
import ipaddress

# list(range(port_min, port_max + 1))

# Function that returns a enum of the user specified scan type
def parse_scan_type(scan_type:str):
    scan_input  = scan_type.strip().upper()
    try:
        return VALID_SCAN_TYPES_MAP[scan_input]
    except KeyError:
        raise ValueError(ERROR_SCANTYPE) from None

# Function that returns a list of ports after parsing that can be used for a scan - will raise a value error if input doesnt match data type
def parse_ports(min_port,max_port):
    return int(min_port),int(max_port)

# Function that returns a float timeout value - will raise a value error if input doesnt match data type
def parse_timeout(timeout):
    return float(timeout)
    
# Function that returns an ip address - will raise a value error if input doesnt match data type
def parse_ip_address(ip_address) :
    return str(ipaddress.ip_address(ip_address))