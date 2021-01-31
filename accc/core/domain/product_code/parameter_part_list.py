from dataclasses import InitVar, dataclass, field

from accc.core.domain.product_code.parameter_part import ParameterPart
from accc.core.domain.product_code.parsed_data import ParsedData


@dataclass
class ParameterPartList:
    value: list[ParameterPart] = field(default_factory=list, init=False)
    parsed_data: InitVar[list[ParsedData]]

    def __post_init__(self, parsed_data: list[ParsedData]):
        """
        >>> N: int
        >>> A: int, B: int
        >>> X: list[int]
        >>> Y: list[A: int, B: int, C: int]
        >>>
        N: int
        A: int, B: int
        X: List[int]
        Y: List[Tuple[int, int, int]]
        """

        for pd in parsed_data:
            self.value.append(ParameterPart(pd))

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self.value.__iter__()
