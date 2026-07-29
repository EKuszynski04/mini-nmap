# Outputs used to display various messages to the user

from .prompts import get_scan_config

def display_menu():
    quit

# Displays the scan configurattion the user inputted
def  display_scan_config():
    scan_config = get_scan_config()

    print("TARGET IP : " + scan_config['ip'])
    print("PORTS : " + scan_config['min_port'] + '-' + scan_config['max_port'])
    print("SCAN : " + scan_config['scan_type'])
    print("TIMEOUT : " + str(scan_config['timeout']))

def warn_user(warning: str):
    print(warning)
    if warning == '1':
        return True
    else:
        return False
