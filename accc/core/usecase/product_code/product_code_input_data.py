from dataclasses import dataclass


@dataclass
class ProductCodeInputData:
    file_name: str
    raw_data: list[str]
