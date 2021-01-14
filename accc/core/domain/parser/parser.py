from dataclasses import dataclass


@dataclass
class Response:
    args: str
    type: str


class Parser:
    def __divide_into_arg_and_type(self, value: str):
        return tuple(x.strip() for x in value.split(":"))

    def __mono_type_parse(self, value: str):
        divided = self.__divide_into_arg_and_type(value)

        return Response(
            divided[0].upper(),
            divided[1],
        )

    def __tuple_type_parse(self, value: str):
        args: list[str] = []
        types: list[str] = []

        for s in [v.strip() for v in value.split(",") if v]:
            parsed = self.__divide_into_arg_and_type(s)
            args.append(parsed[0].upper())
            types.append(parsed[1])

        if len(set(types)) != 1:
            raise ValueError

        return Response(
            ", ".join(args),
            f"Tuple[{', '.join([x for x in types])}]",
        )

    def __list_type_parse(self, value: str):
        divided = self.__divide_into_arg_and_type(value)

        return Response(
            divided[0].upper(),
            "".join(divided[1].split(" ")).capitalize(),
        )

    def __tuple_list_type_parse(self, value: str):
        divided = self.__divide_into_arg_and_type(value)

        inner_type = ":".join(divided[1:]).split("[")[1].split("]")[0]
        tuple_type = self.__tuple_type_parse(inner_type).type

        return Response(
            divided[0],
            f"List[{tuple_type}]",
        )

    def parse(self, value: str) -> Response:
        value = "".join(value.split(" "))
        in_list = "list" in value or "List" in value
        in_tuple = "," in value

        if in_list and in_tuple:
            return self.__tuple_list_type_parse(value)
        elif in_list:
            return self.__list_type_parse(value)
        elif in_tuple:
            return self.__tuple_type_parse(value)
        else:
            return self.__mono_type_parse(value)
