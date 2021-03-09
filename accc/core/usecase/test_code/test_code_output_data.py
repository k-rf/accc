from dataclasses import dataclass
from typing import List


@dataclass
class TestCodeOutputData:
    file_name: str
    product_code_name: str
    readables: List[str]
    expectations: List[str]
