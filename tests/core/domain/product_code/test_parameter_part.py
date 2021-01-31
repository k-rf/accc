import pytest
from accc.core.domain.product_code.parameter_part import ParameterPart
from accc.core.domain.product_code.parsed_data import ParsedData


def ids(value: list[tuple[ParsedData, str]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


class Test_仮引数形式に変換するArgumentConverterクラス:
    class Test_初期化時に仮引数形式に変換する:
        class Test_数値型の仮引数形式に変換する:
            cases = [
                (ParsedData("X", "int"), "X: int"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ParameterPart(args)) == expected

        class Test_数値型タプルの仮引数形式に変換する:
            cases = [
                (ParsedData("X, Y", "Tuple[int, int]"), "X: int, Y: int"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ParameterPart(args)) == expected

        class Test_数値型リストの仮引数形式に変換する:
            cases = [
                (ParsedData("X", "List[int]"), "X: List[int]"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ParameterPart(args)) == expected

        class Test_文字列型の仮引数形式に変換する:
            cases = [
                (ParsedData("X", "str"), "X: str"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ParameterPart(args)) == expected

        class Test_文字列型タプルの仮引数形式に変換する:
            cases = [
                (ParsedData("X, Y", "Tuple[str, str]"), "X: str, Y: str"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ParameterPart(args)) == expected

        class Test_文字列型リストの仮引数形式に変換する:
            cases = [
                (ParsedData("X", "List[str]"), "X: List[str]"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ParameterPart(args)) == expected

        class Test_タプル型リストの仮引数形式に変換する:
            cases = [
                (ParsedData("X", "List[Tuple[int, int]]"), "X: List[Tuple[int, int]]"),
                (ParsedData("X", "List[Tuple[str, str]]"), "X: List[Tuple[str, str]]"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ParameterPart(args)) == expected
