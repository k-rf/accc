from dataclasses import dataclass
from typing import List


@dataclass
class ProductCodeInputData:
    file_name: str
    raw_data: List[str]
