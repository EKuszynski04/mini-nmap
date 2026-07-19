from dataclasses import dataclass
from models import PortState

@dataclass
class ValidationResult:
    valid: bool
    reason: str = ''
    warning: str = ''

    