from .input_parser_response import InputParserResponse


class InputParser:
    def __is_unsupported_type(self, value: str):
        return value not in ("int", "str")

    def __has_no_bracket(self, value: str):
        a = "[" in value
        b = "]" in value
        c = value.index("[") < value.index("]")

        return not (a and b and c)

    def __has_white_space(self, value: str):
        return len(value.split(" ")) > 1

    def __expose_inner_type(self, value: str):
        return value.split("[")[1].split("]")[0].strip()

    def __divide_into_arg_and_type(self, value: str):
        splitted = [x.strip() for x in value.split(":")]
        return tuple([splitted[0], ":".join(splitted[1:])])

    def __mono_type_parse(self, value: str):
        _args, _type = self.__divide_into_arg_and_type(value)

        if self.__has_white_space(_args):
            raise ValueError

        if self.__is_unsupported_type(_type):
            raise ValueError

        return InputParserResponse(_args.upper(), _type)

    def __tuple_type_parse(self, value: str):
        args: list[str] = []
        types: list[str] = []

        for s in [v.strip() for v in value.split(",") if v]:
            _args, _type = self.__divide_into_arg_and_type(s)

            if self.__is_unsupported_type(_type):
                raise ValueError

            args.append(_args.upper())
            types.append(_type)

        if len(set(types)) != 1:
            raise ValueError

        return InputParserResponse(
            ", ".join(args), f"Tuple[{', '.join([x for x in types])}]"
        )

    def __list_type_parse(self, value: str):
        if self.__has_no_bracket(value):
            raise ValueError

        _args, _type = self.__divide_into_arg_and_type(value)

        if self.__is_unsupported_type(self.__expose_inner_type(_type)):
            raise ValueError

        return InputParserResponse(
            _args.upper(), "".join(_type.split(" ")).capitalize()
        )

    def __tuple_list_type_parse(self, value: str):
        _args, _type = self.__divide_into_arg_and_type(value)

        if self.__has_no_bracket(_type):
            raise ValueError

        inner_type = self.__expose_inner_type(_type)
        tuple_type = self.__tuple_type_parse(inner_type).type

        return InputParserResponse(_args, f"List[{tuple_type}]")

    def parse(self, value: str) -> InputParserResponse:
        is_list = "list" in value or "List" in value
        is_tuple = "," in value

        if is_list and is_tuple:
            return self.__tuple_list_type_parse(value)
        elif is_list:
            return self.__list_type_parse(value)
        elif is_tuple:
            return self.__tuple_type_parse(value)
        else:
            return self.__mono_type_parse(value)
