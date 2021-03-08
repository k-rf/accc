from dataclasses import InitVar, dataclass, field
from accc.core.domain.product_code.file_name import FileName
from accc.core.domain.test_code.parsed_data import ParsedData
from accc.core.domain.test_code.readable_list import ReadableList


@dataclass
class TestCode:
    file_name: FileName
    parsed_data: InitVar[list[ParsedData]]
    readables: ReadableList = field(init=False)

    def __post_init__(self, parsed_data: list[ParsedData]):
        self.readables = ReadableList(parsed_data)
