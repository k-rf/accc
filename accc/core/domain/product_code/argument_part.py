from dataclasses import InitVar, dataclass, field

from accc.core.domain.product_code.parsed_data import ParsedData


@dataclass
class ArgumentPart:
    value: str = field(init=False)
    parsed_data: InitVar[ParsedData]

    def __post_init__(self, parsed_data: ParsedData):
        self.value = parsed_data.args

    def __str__(self):
        return self.value
