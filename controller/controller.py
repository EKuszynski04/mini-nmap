# Controller is responsible for orchestrating all the functions and inputs together 
# for the program to work.

from cli.prompts import get_target_ip,get_target_min_port,get_target_max_port,get_prompt_scan_type,get_prompt_timeout
from utils.parses import parse_ip_address, parse_ports , parse_scan_type, parse_timeout
from utils.validators import validate_ports,validate_timeout
from utils.constants import (
    ERROR_IP_INVALID,
    ERROR_PORT_INVALID,
    ERROR_SCANTYPE,
    ERROR_TIMEOUT_INPUT,
    GENERIC_PORT_MSG,
    GENERIC_STATE_MSG,
    GENERIC_ERRMSG_MSG,
    INTRO_BANNER,
    WARNING_USER_MSG,)
from models.scan_config import ScanConfig,ScanType
from scanner.tcp_scanner import tcp_scan
from scanner.udp_scanner import udp_scan

class ScanController:

    def run(self):

        self.show_intro()

        config = self.get_scan_config()

        if config is None:
            return

        results = self.run_scan(config)

        self.display_results(results)


    # Gather all the prompts for a scan config.
    def get_scan_config(self):
        ip = self.get_scan_ip_address()
        ports = self.get_ports()
        scan_type = self.get_scan_type()
        timeout = self.get_timeout()

        return ScanConfig(
            ip=ip,
            ports=ports,
            scan_type=scan_type,
            timeout=timeout)

    # Run udp or tcp scans based on config.
    def run_scan(self, config):
        if config.scan_type == ScanType.TCP:
            return tcp_scan(config.ip,config.ports,config.timeout)
        else:
            return udp_scan(config.ip,config.ports,config.timeout)

    # Display scan results
    def display_results(self, results):
        for scan in results:
            print(
            f"{GENERIC_PORT_MSG} {scan.port} "
            f"{GENERIC_STATE_MSG} {scan.state.value}")
            if scan.error_msg:
                print(f"{GENERIC_ERRMSG_MSG} {scan.error_msg}")

    # Display intro banner and network warning.
    def show_intro(self):
        print(INTRO_BANNER)
        print('\n\n')
        print(WARNING_USER_MSG)

    # Get user inputted ip address and validate ip
    def get_scan_ip_address(self):
        while True:
            ip = get_target_ip()
            try:
                return parse_ip_address(ip)
            except ValueError:
                print(ERROR_IP_INVALID)
                continue
                
    # Retrieves both min and max ports from user inputs and validate
    def get_ports(self):
        while True:
            min_port = get_target_min_port()
            max_port = get_target_max_port()
            try:
                min_port, max_port = parse_ports(min_port, max_port)
            except ValueError:
                print(ERROR_PORT_INVALID)
                continue
            valid = validate_ports(min_port, max_port)
            if not valid.valid:
                print(valid.reason)
                continue
            if valid.warning:
                print(valid.warning)
            return list(range(min_port, max_port + 1))

    # Function to rerieve scan type from user and parse
    def get_scan_type(self):
        while True:
            scantype = get_prompt_scan_type()
            try:
                return parse_scan_type(scantype)
            except ValueError:
                print(ERROR_SCANTYPE)
                continue

    
    # Function to rerieve timeout value from user and validate
    def get_timeout(self):
         while True:
            timeout = get_prompt_timeout()
            try:
                timeout = parse_timeout(timeout)
            except ValueError:
                print(ERROR_TIMEOUT_INPUT)
                continue
            valid = validate_timeout(timeout)
            if not valid.valid:
                print(valid.reason)
                continue
            if valid.warning:
                print(valid.warning)
            return timeout


