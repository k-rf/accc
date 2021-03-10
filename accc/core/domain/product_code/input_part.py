from accc.core.domain.product_code.parsed_data import ParsedData
from dataclasses import InitVar, dataclass, field


@dataclass
class InputPart:
    value: str = field(init=False)
    parsed_data: InitVar[ParsedData]

    def __post_init__(self, parsed_data: ParsedData):
        self.value = self.__convert(parsed_data)

    def __str__(self):
        return self.value

    @staticmethod
    def __convert(value: ParsedData):
        is_tuple = "Tuple" in value.type
        is_list = "List" in value.type
        is_str = "str" in value.type
        is_int = "int" in value.type

        if is_tuple and is_list and is_int:
            return "\n    ".join(
                [
                    f"{value.args} = []",
                    f"for _ in range({value.option}):",
                    f"    {value.args}.append(tuple([int(x) for x in input().split()]))",
                ]
            )

        if is_tuple and is_list and is_str:
            return "\n    ".join(
                [
                    f"{value.args} = []",
                    f"for _ in range({value.option}):",
                    f"    {value.args}.append(tuple([x for x in input().split()]))",
                ]
            )

        if is_tuple and is_int:
            return f"{value.args} = [int(x) for x in input().split()]"

        if is_tuple and is_str:
            return f"{value.args} = [x for x in input().split()]"

        if is_list and is_int:
            return f"{value.args} = [int(x) for x in input().split()]"

        if is_list and is_str:
            return f"{value.args} = [x for x in input().split()]"

        if is_int:
            return f"{value.args} = int(input())"

        if is_str:
            return f"{value.args} = input()"

        raise ValueError(f'"{value.type}" is not supported.')
