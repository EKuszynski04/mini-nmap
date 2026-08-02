# Input handler used to validate and parse user inputs before they get
# processed by the scanner functions

from utils.constants import PROMPT_TARGET_IP,PROMPT_TARGET_MIN_PORT,PROMPT_TARGET_MAX_PORT,PROMPT_SCAN_TYPE,ERROR_PORT_INVALID,PROMPT_TIMEOUT,ERROR_TIMEOUT_INPUT
from utils.validators import validate_scan_type,validate_ip_address,validate_timeout

# Function used to get target ip from user whilst also validating the input and checking for warning and errors
def get_target_ip():
    ip = input(PROMPT_TARGET_IP).strip()
    valid = validate_ip_address(ip)
    if valid.valid is True and not valid.warning:
        return ip
    elif valid.valid is True and valid.warning:
        print(valid.warning)
        return ip
    else:
        return print(valid.reason)

# Function used to get minimum port number from the user whilst also validating the input for potential type errors
def get_target_min_port():
    port_input = input(PROMPT_TARGET_MIN_PORT)
    try:
        port = int(port_input)
        return port
    except ValueError:
        return print(ERROR_PORT_INVALID)


# Function used to get maximum port number from the user whilst also validating the input for potential type errors
def get_target_max_port():
    port_input = input(PROMPT_TARGET_MAX_PORT)
    try:
        port = int(port_input)
        return port
    except ValueError:
        return print(ERROR_PORT_INVALID)

# Function used to get the scan type whilst also validating the input
def get_scan_type():
    scan_type = input(PROMPT_SCAN_TYPE).strip()
    # valid = validate_scan_type(scan_type)
    # if valid.valid is True and not valid.warning:
    #     return scan_type
    # else:
    #     return print(valid.reason)

# Function used to get the timeout float whilst also validating the input
def get_timeout():
    timeout_input = input(PROMPT_TIMEOUT)
    try:
        timeout = float(timeout_input)
    except ValueError:
        return print(ERROR_TIMEOUT_INPUT)
    valid = validate_timeout(timeout)
    if not valid.valid:
        return valid.reason
    if valid.warning:
        print(valid.warning)
    return timeout
