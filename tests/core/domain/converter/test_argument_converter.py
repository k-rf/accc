import pytest
from accc.core.domain.converter.argument_converter import ArgumentConverter
from accc.core.domain.converter.argument_converter_response import (
    ArgumentConverterResponse,
)
from accc.core.domain.parser.input_parser_response import InputParserResponse


def ids(value: list[tuple[InputParserResponse, ArgumentConverterResponse]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


@pytest.fixture
def converter():
    return ArgumentConverter()


class Test_引数形式に変換するArgumentConverterクラス:
    class Test_convertメソッドはInputParserResponseを引数形式に変換する:
        class Test_数値型の引数形式に変換する:
            cases = [
                (InputParserResponse("X", "int"), ArgumentConverterResponse("X: int")),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ArgumentConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_数値型タプルの引数形式に変換する:
            cases = [
                (
                    InputParserResponse("X, Y", "Tuple[int, int]"),
                    ArgumentConverterResponse("X: int, Y: int"),
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ArgumentConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_数値型リストの引数形式に変換する:
            cases = [
                (
                    InputParserResponse("X", "List[int]"),
                    ArgumentConverterResponse("X: List[int]"),
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ArgumentConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_文字列型の引数形式に変換する:
            cases = [
                (InputParserResponse("X", "str"), ArgumentConverterResponse("X: str")),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ArgumentConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_文字列型タプルの引数形式に変換する:
            cases = [
                (
                    InputParserResponse("X, Y", "Tuple[str, str]"),
                    ArgumentConverterResponse("X: str, Y: str"),
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ArgumentConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_文字列型リストの引数形式に変換する:
            cases = [
                (
                    InputParserResponse("X", "List[str]"),
                    ArgumentConverterResponse("X: List[str]"),
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ArgumentConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_タプル型リストの引数形式に変換する:
            cases = [
                (
                    InputParserResponse("X", "List[Tuple[int, int]]"),
                    ArgumentConverterResponse("X: List[Tuple[int, int]]"),
                ),
                (
                    InputParserResponse("X", "List[Tuple[str, str]]"),
                    ArgumentConverterResponse("X: List[Tuple[str, str]]"),
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: ArgumentConverter, args, expected):
                assert converter.convert(args) == expected
