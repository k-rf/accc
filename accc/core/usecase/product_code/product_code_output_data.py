from dataclasses import dataclass
from typing import List


# 間接的にドメイン知識が漏れないようにプリミティブ型を使っている
@dataclass
class ProductCodeOutputData:
    file_name: str
    import_parts: List[str]
    parameter_parts: List[str]
    input_parts: List[str]
    argument_parts: List[str]
