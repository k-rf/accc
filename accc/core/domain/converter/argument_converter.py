from accc.core.domain.converter.argument_converter_response import (
    ArgumentConverterResponse,
)
from accc.core.domain.parser.input_parser_response import InputParserResponse


class ArgumentConverter:
    def __expose_inner_type(self, value: str):
        return value.split("[")[1].split("]")[0].strip()

    def convert(self, value: InputParserResponse):
        is_list = "List" in value.type
        is_tuple = "Tuple" in value.type

        if is_list and is_tuple:
            return ArgumentConverterResponse(f"{value.args}: {value.type}")

        if is_tuple:
            inner = self.__expose_inner_type(value.type)

            args: list[str] = []
            for a, t in zip(value.args.split(", "), inner.split(", ")):
                args.append(f"{a}: {t}")
            return ArgumentConverterResponse(", ".join(args))

        return ArgumentConverterResponse(f"{value.args}: {value.type}")
