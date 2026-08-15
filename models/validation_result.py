from dataclasses import dataclass
from models.port_state import PortState

# A class structure that stores the result of the validation functions.
@dataclass
class ValidationResult:
    # Checks if result is valid
    valid: bool
    # If invlaid a reasons is provided
    reason: str = ''
    # If valid but can be a problem a warning is provided
    warning: str = ''

    