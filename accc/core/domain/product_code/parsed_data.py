from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ParsedData:
    args: str
    type: str
    option: Optional[str] = field(default=None)
