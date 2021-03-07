from dataclasses import InitVar, dataclass, field

from accc.core.domain.test_code.parsed_data import ParsedData


@dataclass
class Readable:
    value: str = field(init=False)
    parsed_data: InitVar[ParsedData]

    def __post_init__(self, parsed_data: ParsedData):
        self.value = self.__convert(parsed_data)

    def __str__(self):
        return self.value

    @staticmethod
    def __convert(value: ParsedData):
        return "\n".join(value.args) + "\n\n" + value.expected + "\n"
