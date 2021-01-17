import pytest
from accc.core.domain.converter.import_converter import ImportConverter
from accc.core.domain.converter.import_converter_response import ImportConverterResponse
from accc.core.domain.parser.input_parser_response import InputParserResponse


def ids(value: list[tuple[InputParserResponse, ImportConverterResponse]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


@pytest.fixture
def converter():
    return ImportConverter()


class Test_import形式に変換するImportConverterクラス:
    class Test_convertメソッドはInputParserResponseをimport形式に変換する:
        class Test_リストのimport形式に変換する:
            cases = [
                (
                    InputParserResponse("X", "List[int]"),
                    ImportConverterResponse("from typing import List"),
                ),
                (
                    InputParserResponse("Y", "List[str]"),
                    ImportConverterResponse("from typing import List"),
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ImportConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_タプル型リストのimport形式に変換する:
            cases = [
                (
                    InputParserResponse("X", "List[Tuple[int, int]]"),
                    ImportConverterResponse(
                        "from sys import stdin\nfrom typing import List, Tuple"
                    ),
                ),
                (
                    InputParserResponse("Y", "List[Tuple[str, str]]"),
                    ImportConverterResponse(
                        "from sys import stdin\nfrom typing import List, Tuple"
                    ),
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ImportConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_それ以外のときNoneに変換する:
            cases = [
                (InputParserResponse("X", "int"), ImportConverterResponse(None)),
                (InputParserResponse("X", "str"), ImportConverterResponse(None)),
                (
                    InputParserResponse("X, Y", "Tuple[int, int]"),
                    ImportConverterResponse(None),
                ),
                (
                    InputParserResponse("X, Y", "Tuple[str, str]"),
                    ImportConverterResponse(None),
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ImportConverter, args, expected):
                assert converter.convert(args) == expected
