from dataclasses import dataclass


@dataclass
class TestCodeInputData:
    test_code_name: str
    product_code_name: str
    raw_data: list[tuple[list[str], str]]
