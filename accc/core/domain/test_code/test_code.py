from dataclasses import InitVar, dataclass, field
from typing import List

from accc.core.domain.product_code.file_name import FileName
from accc.core.domain.test_code.expectation_list import ExpectationList
from accc.core.domain.test_code.parsed_data import ParsedData
from accc.core.domain.test_code.readable_list import ReadableList


@dataclass
class TestCode:
    file_name: FileName
    product_code_name: FileName
    parsed_data: InitVar[List[ParsedData]]
    readables: ReadableList = field(init=False)
    expectations: ExpectationList = field(init=False)

    def __post_init__(self, parsed_data: List[ParsedData]):
        self.readables = ReadableList(parsed_data)
        self.expectations = ExpectationList(parsed_data)
