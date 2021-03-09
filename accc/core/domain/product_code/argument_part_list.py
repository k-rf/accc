from dataclasses import InitVar, dataclass, field
from typing import List

from accc.core.domain.product_code.argument_part import ArgumentPart
from accc.core.domain.product_code.parsed_data import ParsedData


@dataclass
class ArgumentPartList:
    value: List[ArgumentPart] = field(default_factory=list, init=False)
    parsed_data: InitVar[List[ParsedData]]

    def __post_init__(self, parsed_data: List[ParsedData]):
        """
        >>> N: int
        >>> A: int, B: int
        >>> X: List[int]
        >>> Y: List[A: int, B: int, C: int]
        >>>
        N
        A, B
        X
        Y
        """

        for pd in parsed_data:
            self.value.append(ArgumentPart(pd))

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self.value.__iter__()
