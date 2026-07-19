from constants import MAX_PORT_NUMBER,MIN_PORT_NUMBER,MAX_PORT_RANGE,ERROR_PORT_INVALID,WARNING_LARGE_PORT
from models import ValidationResult

def validate_ports(min_port,max_port):
    if min_port > max_port:
        min_port, max_port = max_port, min_port

    if min_port < MIN_PORT_NUMBER or max_port > MAX_PORT_NUMBER:
        return ValidationResult(valid=False,reason=ERROR_PORT_INVALID)
    
    if max_port - min_port > MAX_PORT_RANGE:
        return ValidationResult(valid=True,warning=WARNING_LARGE_PORT)
    

def warn_user(warning: str):
    print(warning)
    if warning == '1':
        return True
    else:
        return False