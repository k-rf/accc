from dataclasses import dataclass


@dataclass
class TestCodeOutputData:
    file_name: str
    readables: list[str]
