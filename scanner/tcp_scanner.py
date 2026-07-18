# tcp_scanner responsible for all tcp related code and functions

import socket
import os
from models import ScanResult, PortState

def tcp_scan(ip: str, ports: list[int], timeout: float):
    ports_scanned = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            try:   
                result = s.connect_ex((ip,port))
                if result == 0:
                    ports_scanned.append(ScanResult(port=port,state=PortState.OPEN))
                else:
                    ports_scanned.append(ScanResult(port=port,state=PortState.CLOSED,error_msg=os.strerror(result)))
            except socket.timeout:
                ports_scanned.append(ScanResult(port=port,state=PortState.TIMEOUT,error_msg="Connection Timed Out"))
            except socket.gaierror as err:
                ports_scanned.append(ScanResult(port=port,state=PortState.ERROR,error_msg=str(err)))
            except OSError as err:
                ports_scanned.append(ScanResult(port=port,state=PortState.ERROR,error_msg=str(err)))
    return ports_scanned