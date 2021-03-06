from dataclasses import InitVar, dataclass, field
from typing import List

from accc.core.domain.product_code.input_part import InputPart
from accc.core.domain.product_code.parsed_data import ParsedData


@dataclass
class InputPartList:
    value: List[InputPart] = field(default_factory=list, init=False)
    parsed_data: InitVar[List[ParsedData]]

    def __post_init__(self, parsed_data: List[ParsedData]):
        """
        >>> N: int
        >>> A: int, B: int
        >>> X: List[int]
        >>> Y: List[A: int, B: int, C: int]
        >>>
        N = int(input())
        A, B = [int(x) for x in input().split()]
        X = [int(x) for x in input().split()]
        Y = []
        for line in stdin:
            Y.append(tuple(int(x) for x in line.split()))
        """

        for pd in parsed_data:
            self.value.append(InputPart(pd))

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self.value.__iter__()
