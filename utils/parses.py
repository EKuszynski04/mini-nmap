# Parses.py responsible for parsing different inputs to match 
# different functions datatypes after validations


# Function that returns a list of ports that can be used for a scan
def parse_ports(min_port:int,max_port:int):
    return list(range(min_port, max_port + 1))

# Function used to check reuturn a scan type based on user input
def parse_scan_type(scan_type:str):
    if scan_type == 'T' or scan_type == 'TCP':
        scan = 'TCP'
    else:
        scan = 'UDP'
    return scan