# Constant String Error Messages
ERROR_GENERIC:str = "Error"
ERROR_PORT_INVALID:str = "Invalid port number."
ERROR_PORT_RANGE:str = "Max port number is smaller than minimum port number."
ERROR_IP_INVALID:str = "Invalid IP address."
ERROR_HOST_UNREACHABLE:str = "Host is unreachable."
ERROR_SCANTYPE:str =  "Invalid scan type."
ERROR_IP_INVALID:str =  "Invalid ip address."
ERROR_MAX_TIMEOUT:str = "Invalid timeout value. Maximum timeout exceeded"
ERROR_MIN_TIMEOUT:str = "Invalid timeout value. Minimum timeout exceeded"
ERROR_TIMEOUT_INPUT:str = "Invalid timeout input."
ERROR_TIMEOUT_TEXT:str = "Connection Timed Out"


# Constant String Warning Messages
WARNING_USER_MSG:str = "Warning: Only scan systems where you have explict permission."
WARNING_LARGE_SCAN:str = "Warning: Port Range used is quite large therefore will result in large waiting times."
WARNING_LARGE_PORT_RANGE:str = "Warning: Large port number detected."
WARNING_LARGE_TIMEOUT:str = "Warning: Long timeout time detected."


# Constant Information Messages
INFO_SCAN_STARTED:str = "Starting scan..."
INFO_SCAN_COMPLETE:str = "Scan completed."

# Constant Generic Messages
GENERIC_PORT_MSG:str = "Port: "
GENERIC_STATE_MSG:str = "State: "
GENERIC_ERRMSG_MSG:str = "Error Message: "

# Constant Confirmation Messages
YN_CONF_MESSAGE:str = "(Y)es to proceed. (N)o to cancel. (Y/N)..."

# Constant Port Numbers
MIN_PORT_NUMBER:int = 1
MAX_PORT_NUMBER:int = 65535
MAX_PORT_RANGE:int =  5000
COMMON_PORT_LIMIT: int = 1024

# Constant Timeout Times
COMMON_TIMEOUT_LIMIT:float = 1.0
MAX_TIMEOUT_LIMIT:float = 3.0
MIN_TIMEOUT_LIMIT:float = 0.01

# Constant Prompt Strings
PROMPT_TARGET_IP:str = "Target IP address: "
PROMPT_TARGET_MIN_PORT:str = "Target Minimum Port: "
PROMPT_TARGET_MAX_PORT:str = "Target Maximum Port: "
PROMPT_SCAN_TYPE:str = "Scan type - (T)CP or (U)DP: "
PROMPT_TIMEOUT:str = "Timeout Amount: "

# Constant User Warning
WARNING_USER_MSG = (
    "[!] LEGAL & ETHICAL USE\n"
    "Mini Nmap is intended for educational purposes and authorised "
    "security testing only.\n"
    "Only scan systems and networks that you have explicit permission "
    "to test. Unauthorised scanning may be illegal.\n"
    "By continuing, you acknowledge that you are responsible for "
    "ensuring that your use of this tool is lawful and authorised."
)

# Constant Intro Banner
INTRO_BANNER = (r""" 
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

███╗░░░███╗██╗███╗░░██╗██╗███╗░░██╗███╗░░░███╗░█████╗░██████╗░
████╗░████║██║████╗░██║██║████╗░██║████╗░████║██╔══██╗██╔══██╗
██╔████╔██║██║██╔██╗██║██║██╔██╗██║██╔████╔██║███████║██████╔╝
██║╚██╔╝██║██║██║╚████║██║██║╚████║██║╚██╔╝██║██╔══██║██╔═══╝░
██║░╚═╝░██║██║██║░╚███║██║██║░╚███║██║░╚═╝░██║██║░░██║██║░░░░░
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░""")
