# udp_scanner responsible for all udp related code and functions 

import socket
import os
from models import ScanResult, PortState

# UDP scan function takes in the ipaddress,ports and timeout variable. 
# Tries to establish a connection with each port specififed in the list and 
# returns a list of ScanResult objects based on results
def udp_scan(ip: str, ports: list[int], timeout: float):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        ports_scanned = []
        for port in ports:
            try:   
                result = s.connect_ex((ip,port))
                # if connection is succeffull port is open
                if result == 0:
                    ports_scanned.append(ScanResult(port=port,state=PortState.OPEN))
                else:
                    ports_scanned.append(ScanResult(port=port,state=PortState.CLOSED,error_msg=os.strerror(result)))
            except socket.timeout:
                ports_scanned.append(ScanResult(port=port,state=PortState.TIMEOUT,error_msg="Connection Timed Out"))
            # Subclass of OSErrors resolving hostname specific (for future hostname scans)
            except socket.gaierror as err:
                ports_scanned.append(ScanResult(port=port,state=PortState.ERROR,error_msg=str(err)))
            # Operating System related Errors
            except OSError as err:
                ports_scanned.append(ScanResult(port=port,state=PortState.ERROR,error_msg=str(err)))
        return ports_scanned
        


