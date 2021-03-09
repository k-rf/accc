from dataclasses import InitVar, dataclass, field

from accc.core.domain.test_code.expectation import Expectation
from accc.core.domain.test_code.parsed_data import ParsedData


@dataclass
class ExpectationList:
    value: list[Expectation] = field(default_factory=list, init=False)
    parsed_data: InitVar[list[ParsedData]]

    def __post_init__(self, parsed_data: list[ParsedData]):
        for pd in parsed_data:
            self.value.append(Expectation(pd))

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self.value.__iter__()
