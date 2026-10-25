# udp_scanner responsible for all udp related code and functions 

import socket
import os
from models.scan_result import ScanResult
from models.port_state import  PortState
from utils.constants import (ERROR_TIMEOUT_TEXT)

# UDP scan function takes in the ipaddress,ports and timeout variable. 
# Tries to establish a connection with each port specififed in the list and 
# returns a list of ScanResult objects based on results
def udp_scan(ip: str, ports: list[int], timeout: float):
    ports_scanned = []
    for port in ports:

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(timeout)
            
            try:
                s.connect((ip,port))
                s.sendto(b"MININMAP", (ip,port))

                data,address = s.recvfrom(1024)

                ports_scanned.append(ScanResult(port=port,state=PortState.OPEN))
            except ConnectionRefusedError:
                ports_scanned.append(ScanResult(port=port,state=PortState.CLOSED))
            except socket.timeout:
                ports_scanned.append(ScanResult(port=port,state=PortState.TIMEOUT,error_msg=ERROR_TIMEOUT_TEXT))
            # Subclass of OSErrors resolving hostname specific (for future hostname scans implementation)
            except socket.gaierror as err:
                ports_scanned.append(ScanResult(port=port,state=PortState.ERROR,error_msg=str(err)))
            # Operating System related Errors
            except OSError as err:
                ports_scanned.append(ScanResult(port=port,state=PortState.ERROR,error_msg=str(err)))
        return ports_scanned
        


