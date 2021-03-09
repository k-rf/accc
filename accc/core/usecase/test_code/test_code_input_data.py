from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCodeInputData:
    test_code_name: str
    product_code_name: str
    raw_data: List[Tuple[List[str], str]]
