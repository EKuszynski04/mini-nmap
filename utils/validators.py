# Validators used to vaidate various user inputs and provide feedback

from constants import MAX_PORT_NUMBER,MIN_PORT_NUMBER,MAX_PORT_RANGE,ERROR_PORT_INVALID,WARNING_LARGE_PORT,VALID_SCAN_TYPES,ERROR_SCANTYPE
from models import ValidationResult

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
def validate_scan_type(scan_input:str):
    scan_input = scan_input.upper()
    if scan_input in VALID_SCAN_TYPES:
        return ValidationResult(valid=True,warning=WARNING_LARGE_PORT)
    return ValidationResult(valid=False, reason=ERROR_SCANTYPE)