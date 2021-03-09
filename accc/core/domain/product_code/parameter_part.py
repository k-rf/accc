from dataclasses import InitVar, dataclass, field

from accc.core.domain.product_code.parsed_data import ParsedData


@dataclass
class ParameterPart:
    value: str = field(init=False)
    parsed_data: InitVar[ParsedData]

    def __post_init__(self, parsed_data: ParsedData):
        self.value = self.__convert(parsed_data)

    def __str__(self):
        return self.value

    @staticmethod
    def __expose_inner_type(value: str):
        return value.split("[")[1].split("]")[0].strip()

    @staticmethod
    def __convert(value: ParsedData):
        is_list = "List" in value.type
        is_tuple = "Tuple" in value.type

        if is_list and is_tuple:
            return f"{value.args.lower()}: {value.type}"

        if is_tuple:
            inner = ParameterPart.__expose_inner_type(value.type)

            args: list[str] = []
            for a, t in zip(value.args.split(", "), inner.split(", ")):
                args.append(f"{a.lower()}: {t}")
            return ", ".join(args)

        return f"{value.args.lower()}: {value.type}"
