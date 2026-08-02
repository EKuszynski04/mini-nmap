# Controller is responsible for orchestrating all the functions and inputs together 
# for the program to work.

from cli.prompts import get_target_ip,get_target_min_port,get_target_max_port,get_scan_type,get_timeout

# 1. controller
# 2. prompts
# 3. parsers
# 4. validators

class ScanController:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def run(self):

        self.show_intro()

        config = self.get_scan_config()

        if config is None:
            return

        results = self.run_scan(config)

        self.display_results(results)


    # Function used gather all the prompts for a scan.
    def get_scan_config(self):
        quit # placeholder

    def run_scan(self, config):
        quit  # placeholder

    def display_results(self, config):
        quit  # placeholder

    def show_intro(self):
        quit  # placeholder

    

# def get_scan_config():
#     ip_address = get_target_ip()
#     min_port = get_target_min_port()
#     max_port = get_target_max_port()
#     scan_type = get_scan_type()
#     return {'ip': ip_address or '192.168.100.20',
#             'min_port': min_port,
#             'max_port': max_port,
#             'timeout': 1,
#             'scan_type': scan_type}
