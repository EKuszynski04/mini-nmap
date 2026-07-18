# udp_scanner responsible for all udp related code and functions 

import socket;

def udp_scan(ip, ports, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        res = s.connect_ex((ip,ports))
        s.setsockopt(timeout)
        if res == 0:
            return 'port is open'
        else:
            return res


