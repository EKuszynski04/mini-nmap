# Constant String Error Messages
ERROR_PORT_INVALID:str = "Invalid port number."
ERROR_IP_INVALID:str = "Invalid IP address."
ERROR_HOST_UNREACHABLE:str = "Host is unreachable."
ERROR_SCANTYPE:str =  "Invalid scan type."

# Constant String Warning Messages
WARNING_USER_MSG:str = "Warning: Only scan systems where you have explict permission."
WARNING_LARGE_SCAN:str = "Warning: Port Range used is quite large therefore will result in large waiting times."
WARNING_LARGE_PORT:str = "Warning: Large port number detected is that correct?"

# Constant Information Messages
INFO_SCAN_STARTED:str = "Starting scan..."
INFO_SCAN_COMPLETE:str = "Scan completed."

# Constant Confirmation Messages
YN_CONF_MESSAGE:str = "(Y)es to proceed. (N)o to cancel. (Y/N)..."

# Constant Port Numbers
MIN_PORT_NUMBER:int = 1
MAX_PORT_NUMBER:int = 65535
MAX_PORT_RANGE:int =  5000
COMMON_PORT_LIMIT: int = 1024

# Constant Prompt Strings
PROMPT_TARGET_IP:str = "Target IP address: "
PROMPT_TARGET_MIN_PORT:str = "Target Port: "
PROMPT_TARGET_MAX_PORT:str = "Target Port: "
PROMPT_SCAN_TYPE:str = "Scan type - (T)CP or (U)DP: "

# Constant Valid Scan Types Collection
VALID_SCAN_TYPES = {"T", "TCP", "U", "UDP"}