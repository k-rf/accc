from typing import List, Tuple
import pytest
from accc.core.domain.product_code.parsed_data import ParsedData
from accc.core.domain.product_code.argument_part import ArgumentPart


def ids(value: List[Tuple[ParsedData, str]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


class Test_引数形式に変換するArgumentPartクラス:
    class Test_初期化時に引数形式に変換する:
        class Test_数値型の引数形式に変換する:
            cases = [
                (ParsedData("X", "int"), "X"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ArgumentPart(args)) == expected

        class Test_数値型リストの引数形式に変換する:
            cases = [
                (ParsedData("X", "List[int]"), "X"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ArgumentPart(args)) == expected

        class Test_数値型タプルの引数形式に変換する:
            cases = [
                (ParsedData("X, Y", "Tuple[int, int]"), "X, Y"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ArgumentPart(args)) == expected

        class Test_文字列型の引数形式に変換する:
            cases = [
                (ParsedData("X", "str"), "X"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ArgumentPart(args)) == expected

        class Test_文字列型リストの引数形式に変換する:
            cases = [
                (ParsedData("X", "List[str]"), "X"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ArgumentPart(args)) == expected

        class Test_文字列型タプルの引数形式に変換する:
            cases = [
                (ParsedData("X", "Tuple[str, str]"), "X"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ArgumentPart(args)) == expected

        class Test_タプル型リストの引数形式に変換する:
            cases = [
                (ParsedData("X", "List[Tuple[int, int]]"), "X"),
                (ParsedData("X", "List[Tuple[str, str]]"), "X"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ArgumentPart(args)) == expected
