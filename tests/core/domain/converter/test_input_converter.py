import pytest
from accc.core.domain.converter.input_converter import InputConverter
from accc.core.domain.parser.input_parser_response import InputParserResponse


def ids(value: list[tuple[InputParserResponse, str]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


@pytest.fixture
def converter():
    return InputConverter()


class Test_入力形式に変換するInputConverterクラス:
    class Test_convertメソッドはInputParserResponseを入力形式に変換する:
        class Test_数値型の入力形式に変換する:
            cases = [
                (InputParserResponse("X", "int"), "X = int(input())"),
                (InputParserResponse("Y", "int"), "Y = int(input())"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: InputConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_数値型タプルの入力形式に変換する:
            cases = [
                (
                    InputParserResponse("X, Y", "Tuple[int, int]"),
                    "X, Y = [int(x) for x in input().split()]",
                ),
                (
                    InputParserResponse("X, Y, Z", "Tuple[int, int, int]"),
                    "X, Y, Z = [int(x) for x in input().split()]",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: InputConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_数値型リストの入力形式に変換する:
            cases = [
                (
                    InputParserResponse("X", "List[int]"),
                    "X = [int(x) for x in input().split()]",
                ),
                (
                    InputParserResponse("Y", "List[int]"),
                    "Y = [int(x) for x in input().split()]",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: InputConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_文字列型の入力形式に変換する:
            cases = [
                (InputParserResponse("X", "str"), "X = input()"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: InputConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_文字列型タプルの入力形式に変換する:
            cases = [
                (
                    InputParserResponse("X, Y", "Tuple[str, str]"),
                    "X, Y = [x for x in input().split()]",
                ),
                (
                    InputParserResponse("X, Y, Z", "Tuple[str, str, str]"),
                    "X, Y, Z = [x for x in input().split()]",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: InputConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_文字列型リストの入力形式に変換する:
            cases = [
                (
                    InputParserResponse("X", "List[str]"),
                    "X = [x for x in input().split()]",
                ),
                (
                    InputParserResponse("Y", "List[str]"),
                    "Y = [x for x in input().split()]",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: InputConverter, args, expected):
                assert converter.convert(args) == expected

        class Test_タプル型リストの入力形式に変換する:
            cases = [
                (
                    InputParserResponse("X", "List[Tuple[int, int]]"),
                    "X = []\n"
                    "for line in stdin:\n"
                    "    X.append(tuple([int(x) for x in line.split()]))",
                ),
                (
                    InputParserResponse("Y", "List[Tuple[str, str]]"),
                    "Y = []\n"
                    "for line in stdin:\n"
                    "    Y.append(tuple([x for x in line.split()]))",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, converter: InputConverter, args, expected):
                assert converter.convert(args) == expected
