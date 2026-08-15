# Prompts used to provide the user with various different prompts

from utils.constants import PROMPT_TARGET_IP,PROMPT_TARGET_MIN_PORT,PROMPT_TARGET_MAX_PORT,PROMPT_SCAN_TYPE,PROMPT_TIMEOUT

# Function user to prompt the user to enter ip address of target
def get_target_ip():
    return input(PROMPT_TARGET_IP).strip()

# Function user to prompt the user to enter minimum port value in the port range
def get_target_min_port():
    return input(PROMPT_TARGET_MIN_PORT)

# Function user to prompt the user to enter maximum port value in the port range
def get_target_max_port():
    return input(PROMPT_TARGET_MAX_PORT)

# Function user to prompt the user to enter the scan type tahts going to be used
def get_prompt_scan_type():
    return input(PROMPT_SCAN_TYPE)

# Function user to prompt the user to enter the timeout value for each port
def get_prompt_timeout():
    return input(PROMPT_TIMEOUT)

# def get_scan_config():
#     ip_address = get_target_ip()
#     min_port = get_target_min_port()
#     max_port = get_target_max_port()
#     scan_type = get_scan_type()
#     return {'ip': ip_address or '192.168.100.20',
#             'min_port': min_port,
#             'max_port': max_port,
#             'timeout': 1,
#             'scan_type': scan_type}

