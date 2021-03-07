from dataclasses import InitVar, dataclass, field
from accc.core.domain.test_code.readable import Readable
from accc.core.domain.test_code.parsed_data import ParsedData


@dataclass
class ReadableList:
    value: list[Readable] = field(default_factory=list, init=False)
    parse_data: InitVar[list[ParsedData]]

    def __post_init__(self, parsed_data: list[ParsedData]):
        """
        >>>
        2
        1 2 3
        4 5 6

        21
        >>>
        3
        1 2 3
        4 5 6
        7 8 9

        45
        """
        for pd in parsed_data:
            self.value.append(Readable(pd))

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self.value.__iter__()
