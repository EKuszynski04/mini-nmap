# tcp_scanner responsible for all tcp related code and functions

import socket
import os
import errno
from models.scan_result import ScanResult
from models.port_state import  PortState
from utils.constants import (ERROR_TIMEOUT_TEXT)

# TCP scan function takes in the ipaddress,ports and timeout variable. 
# Tries to establish a connection with each port specififed in the list and 
# returns a list of ScanResult objects based on results
def tcp_scan(ip: str, ports: list[int], timeout: float):
    ports_scanned = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            try:   
                result = s.connect_ex((ip,port))
                # if connection is succeffull port is open
                if result == 0:
                    ports_scanned.append(ScanResult(port=port,state=PortState.OPEN))
                # connection refused
                elif result == errno.ECONNREFUSED:
                    ports_scanned.append(ScanResult(port=port,state=PortState.CLOSED,error_msg=os.strerror(result)))
                else:
                    ports_scanned.append(ScanResult(port=port,state=PortState.ERROR,error_msg=os.strerror(result)))
            except socket.timeout:
                ports_scanned.append(ScanResult(port=port,state=PortState.TIMEOUT,error_msg=ERROR_TIMEOUT_TEXT))
            # Subclass of OSErrors resolving hostname specific (for future hostname scans implementation)
            except socket.gaierror as err:
                ports_scanned.append(ScanResult(port=port,state=PortState.ERROR,error_msg=str(err)))
            # Operating System related Errors
            except OSError as err:
                ports_scanned.append(ScanResult(port=port,state=PortState.ERROR,error_msg=str(err)))
    return ports_scanned