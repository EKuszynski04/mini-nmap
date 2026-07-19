from .prompts import get_scan_config


def  display_scan_config():
    scan_config = get_scan_config()
    print("TARGET IP : " + scan_config['ip'])
    print("PORTS : " + scan_config['min_port'] + '-' + scan_config['max_port'])
    print("SCAN : " + scan_config['scan_type'])
    print("TIMEOUT : " + str(scan_config['timeout']))

