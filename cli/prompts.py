from utils.constants import PROMPT_TARGET_IP,PROMPT_TARGET_PORT

def get_target_ip():
    return input(PROMPT_TARGET_IP).strip()

def get_target_port():
    return input(PROMPT_TARGET_PORT)

def get_scan_config():
    ip_address = get_target_ip()
    min_port = get_target_port()
    max_port = get_target_port()
    return {'ip': ip_address or '192.168.100.20',
            'min_port': min_port,
            'max_port': max_port,
            'timeout': 1,
            'scan_type': 'tcp'}
