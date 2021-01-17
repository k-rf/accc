from dataclasses import dataclass
from typing import Optional

@dataclass
class ImportConverterResponse:
    value: Optional[str]
