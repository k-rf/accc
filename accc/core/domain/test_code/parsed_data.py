from dataclasses import dataclass


@dataclass
class ParsedData:
    args: list[str]
    expected: str
