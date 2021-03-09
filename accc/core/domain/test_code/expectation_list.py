from dataclasses import InitVar, dataclass, field
from typing import List

from accc.core.domain.test_code.expectation import Expectation
from accc.core.domain.test_code.parsed_data import ParsedData


@dataclass
class ExpectationList:
    value: List[Expectation] = field(default_factory=list, init=False)
    parsed_data: InitVar[List[ParsedData]]

    def __post_init__(self, parsed_data: List[ParsedData]):
        for pd in parsed_data:
            self.value.append(Expectation(pd))

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self.value.__iter__()
