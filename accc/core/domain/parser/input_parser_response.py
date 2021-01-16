from dataclasses import dataclass


@dataclass
class InputParserResponse:
    args: str
    type: str
