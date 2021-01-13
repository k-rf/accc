class Parser:
    def __divide_into_arg_and_type(self, value: str):
        return tuple(x.strip() for x in value.split(":"))

    def __list_type_parse(self, value: str):
        parsed = self.__divide_into_arg_and_type(value)

        return {
            "args": parsed[0].upper(),
            "type": "".join(parsed[1].split(" ")).capitalize(),
        }

    def __mono_type_parse(self, value: str):
        parsed = self.__divide_into_arg_and_type(value)

        return {
            "args": parsed[0].upper(),
            "type": parsed[1],
        }

    def __tuple_type_parse(self, value: list[str]):
        args: list[str] = []
        types: list[str] = []

        for s in [v for v in value if v]:
            parsed = self.__divide_into_arg_and_type(s)
            args.append(parsed[0].upper())
            types.append(parsed[1])

        if len(set(types)) != 1:
            raise ValueError

        return {
            "args": ", ".join(args),
            "type": f"Tuple[{', '.join([x for x in types])}]",
        }

    def parse(self, value: str):
        if len(splitted := value.split(",")) > 1:
            return self.__tuple_type_parse(splitted)
        elif "list" in value or "List" in value:
            return self.__list_type_parse(value)
        else:
            return self.__mono_type_parse(value)
