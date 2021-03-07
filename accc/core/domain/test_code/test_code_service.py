from accc.core.domain.test_code.parsed_data import ParsedData
from typing import Union, overload


class TestCodeService:
    @overload
    def parse(self, value: tuple[list[str], str]) -> ParsedData:
        ...

    @overload
    def parse(self, value: list[tuple[list[str], str]]) -> list[ParsedData]:
        ...

    def parse(self, value: Union[tuple[list[str], str], list[tuple[list[str], str]]]):
        if isinstance(value, tuple):
            return ParsedData("\n".join(value[0]) + f"\n\n{value[1]}\n")
        else:
            return [self.parse(v) for v in value]
