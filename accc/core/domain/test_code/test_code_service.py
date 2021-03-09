from accc.core.domain.test_code.parsed_data import ParsedData
from typing import List, Tuple, Union, overload


class TestCodeService:
    @overload
    def parse(self, value: Tuple[List[str], str]) -> ParsedData:
        ...

    @overload
    def parse(self, value: List[Tuple[List[str], str]]) -> List[ParsedData]:
        ...

    def parse(self, value: Union[Tuple[List[str], str], List[Tuple[List[str], str]]]):
        if isinstance(value, tuple):
            return ParsedData(value[0], value[1])
        else:
            return [self.parse(v) for v in value]
