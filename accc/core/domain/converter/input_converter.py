from accc.core.domain.parser.input_parser_response import InputParserResponse


class InputConverter:
    def convert(self, value: InputParserResponse):
        is_tuple = "Tuple" in value.type
        is_list = "List" in value.type
        is_str = "str" in value.type
        is_int = "int" in value.type

        if is_tuple and is_list and is_int:
            return (
                f"{value.args} = []\n"
                f"for line in stdin:\n"
                f"    {value.args}.append(tuple([int(x) for x in line.split()]))"
            )

        if is_tuple and is_list and is_str:
            return (
                f"{value.args} = []\n"
                f"for line in stdin:\n"
                f"    {value.args}.append(tuple([x for x in line.split()]))"
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
