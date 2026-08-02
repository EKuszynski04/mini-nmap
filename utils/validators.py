# Validators used to vaidate various user inputs and provide feedback

from constants import MAX_PORT_NUMBER,MIN_PORT_NUMBER,MAX_PORT_RANGE,ERROR_PORT_INVALID,WARNING_LARGE_PORT,ERROR_SCANTYPE,ERROR_IP_INVALID,WARNING_LARGE_TIMEOUT,COMMON_TIMEOUT_LIMIT,MAX_TIMEOUT_LIMIT,MIN_TIMEOUT_LIMIT,WARNING_LARGE_TIMEOUT,ERROR_MIN_TIMEOUT,ERROR_MAX_TIMEOUT
from models import ValidationResult,ScanType
import ipaddress

# Functions used to validate the user inputted ports
def validate_ports(min_port:int,max_port:int):
    if min_port > max_port:
        min_port, max_port = max_port, min_port

    if min_port < MIN_PORT_NUMBER or max_port > MAX_PORT_NUMBER:
        return ValidationResult(valid=False,reason=ERROR_PORT_INVALID)
    
    if max_port - min_port > MAX_PORT_RANGE:
        return ValidationResult(valid=True,warning=WARNING_LARGE_PORT)
    return ValidationResult(valid=True)
# Functions used to validate the user inputted scan type
def validate_scan_type(scan_input:ScanType):
    if isinstance (scan_input,ScanType):
        return ValidationResult(valid=True)
    return ValidationResult(valid=False, reason=ERROR_SCANTYPE)

# Function used to validate IP addresses
def validate_ip_address(ip_addr:str):
    try: 
        ipaddress.ip_address(ip_addr)
        return ValidationResult(valid=True)
    except ValueError:
        return ValidationResult(valid=False,reason=ERROR_IP_INVALID)

# Function to validate timeout times
def validate_timeout(timeout:float):
    if timeout < MIN_TIMEOUT_LIMIT:
            return ValidationResult(valid=False,reason=ERROR_MIN_TIMEOUT)
    if timeout > MAX_TIMEOUT_LIMIT:
        return ValidationResult(valid=False,reason=ERROR_MAX_TIMEOUT)
    if timeout > COMMON_TIMEOUT_LIMIT:
        return ValidationResult(valid=True,warning=WARNING_LARGE_TIMEOUT)
    return ValidationResult(valid=True)
