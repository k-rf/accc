from dataclasses import dataclass


@dataclass
class TestCodeInputData:
    file_name: str
    raw_data: list[tuple[list[str], str]]
