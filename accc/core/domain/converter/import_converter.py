from accc.core.domain.converter.import_converter_response import ImportConverterResponse
from accc.core.domain.parser.input_parser_response import InputParserResponse


class ImportConverter:
    def convert(self, value: InputParserResponse):
        is_list = "List" in value.type
        is_tuple = "Tuple" in value.type

        if is_list and is_tuple:
            return ImportConverterResponse(
                "from sys import stdin\nfrom typing import List, Tuple"
            )
        if is_list:
            return ImportConverterResponse("from typing import List")

        return ImportConverterResponse(None)
