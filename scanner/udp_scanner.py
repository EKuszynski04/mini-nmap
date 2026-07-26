# udp_scanner responsible for all udp related code and functions 

import socket;

def udp_scan(ip, ports, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        result = s.connect_ex((ip,ports))
        s.settimeout(timeout)
        if result == 0:
            return 'port is open'
        else:
            return result


