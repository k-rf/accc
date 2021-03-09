from dataclasses import dataclass
from typing import List


@dataclass
class ParsedData:
    args: List[str]
    expectation: str
