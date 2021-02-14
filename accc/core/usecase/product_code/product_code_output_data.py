from dataclasses import dataclass


# 間接的にドメイン知識が漏れないようにプリミティブ型を使っている
@dataclass
class ProductCodeOutputData:
    file_name: str
    import_parts: list[str]
    parameter_parts: list[str]
    input_parts: list[str]
    argument_parts: list[str]
