# Input handler used to validate and parse user inputs before they get
# processed by the scanner functions

from utils.constants import PROMPT_TARGET_IP,PROMPT_TARGET_MIN_PORT,PROMPT_TARGET_MAX_PORT,PROMPT_SCAN_TYPE
from utils.validators import validate_ports,validate_scan_type,validate_ip_address,validate_timeout

def get_target_ip():
    ip = input(PROMPT_TARGET_IP).strip()
    valid = validate_ip_address(ip)
    if valid.valid is True and not valid.warning:
        return ip
    elif valid.valid is True and valid.warning:
        print(valid.warning)
        return ip
    else:
        return print("Error")

def get_target_min_port():
    return input(PROMPT_TARGET_MIN_PORT)

def get_target_max_port():
    port_input = input("Port: ")

    try:
        port = int(port_input)
    except ValueError:
        return print("Port must be a whole number.")
    return port

def get_scan_type():
    return input(PROMPT_SCAN_TYPE)