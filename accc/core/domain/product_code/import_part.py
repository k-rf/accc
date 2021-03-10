from typing import Optional
from accc.core.domain.product_code.parsed_data import ParsedData
from dataclasses import InitVar, dataclass, field


@dataclass(unsafe_hash=True)
class ImportPart:
    value: Optional[str] = field(init=False)
    parsed_data: InitVar[ParsedData]

    def __post_init__(self, parsed_data: ParsedData):
        self.value = self.__convert(parsed_data)

    def __str__(self):
        return self.value

    @staticmethod
    def __convert(value: ParsedData):
        is_list = "List" in value.type
        is_tuple = "Tuple" in value.type

        if is_list and is_tuple:
            return "from typing import List, Tuple"
        if is_list:
            return "from typing import List"

        raise ValueError(f'"{value.type}" is not supported.')
