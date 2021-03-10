from typing import List, Tuple
import pytest
from accc.core.domain.product_code.input_part import InputPart
from accc.core.domain.product_code.parsed_data import ParsedData


def ids(value: List[Tuple[ParsedData, str]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


class Test_プロダクトコードの入力部分を扱うInputPartクラス:
    class Test_初期化時に入力形式に変換する:
        class Test_数値型の入力形式に変換する:
            cases = [
                (ParsedData("X", "int"), "X = int(input())"),
                (ParsedData("Y", "int"), "Y = int(input())"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(InputPart(args)) == expected

        class Test_数値型タプルの入力形式に変換する:
            cases = [
                (
                    ParsedData("X, Y", "Tuple[int, int]"),
                    "X, Y = [int(x) for x in input().split()]",
                ),
                (
                    ParsedData("X, Y, Z", "Tuple[int, int, int]"),
                    "X, Y, Z = [int(x) for x in input().split()]",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(InputPart(args)) == expected

        class Test_数値型リストの入力形式に変換する:
            cases = [
                (
                    ParsedData("X", "List[int]"),
                    "X = [int(x) for x in input().split()]",
                ),
                (
                    ParsedData("Y", "List[int]"),
                    "Y = [int(x) for x in input().split()]",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(InputPart(args)) == expected

        class Test_文字列型の入力形式に変換する:
            cases = [
                (ParsedData("X", "str"), "X = input()"),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(InputPart(args)) == expected

        class Test_文字列型タプルの入力形式に変換する:
            cases = [
                (
                    ParsedData("X, Y", "Tuple[str, str]"),
                    "X, Y = [x for x in input().split()]",
                ),
                (
                    ParsedData("X, Y, Z", "Tuple[str, str, str]"),
                    "X, Y, Z = [x for x in input().split()]",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(InputPart(args)) == expected

        class Test_文字列型リストの入力形式に変換する:
            cases = [
                (
                    ParsedData("X", "List[str]"),
                    "X = [x for x in input().split()]",
                ),
                (
                    ParsedData("Y", "List[str]"),
                    "Y = [x for x in input().split()]",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(InputPart(args)) == expected

        class Test_タプル型リストの入力形式に変換する:
            cases = [
                (
                    ParsedData("X", "List[Tuple[int, int]]", "N"),
                    "X = []\n    "
                    "for _ in range(N):\n    "
                    "    X.append(tuple([int(x) for x in input().split()]))",
                ),
                (
                    ParsedData("Y", "List[Tuple[str, str]]", "M"),
                    "Y = []\n    "
                    "for _ in range(M):\n    "
                    "    Y.append(tuple([x for x in input().split()]))",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(InputPart(args)) == expected
