from dataclasses import asdict

import pytest
from accc.core.domain.parser.parser import Parser


def ids(value: list[tuple[str, dict[str, str]]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


def ids_raise_ValueError(value: list[str]):
    return (f"{x} >> raise ValueError" for x in value)


class Test_文字列を解析するParserクラス:
    class Test_parseメソッドは文字列を解析して辞書型に変換する:
        @pytest.fixture
        def parser(self):
            return Parser()

        class Test_数値型を解析する:
            cases = [
                ("X: int", {"args": "X", "type": "int"}),
                ("X:int", {"args": "X", "type": "int"}),
                ("X :int", {"args": "X", "type": "int"}),
                ("X : int", {"args": "X", "type": "int"}),
                ("x: int", {"args": "X", "type": "int"}),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: Parser, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_数値型タプルを解析する:
            cases = [
                ("X: int, Y: int", {"args": "X, Y", "type": "Tuple[int, int]"}),
                ("X : int , Y:int", {"args": "X, Y", "type": "Tuple[int, int]"}),
                ("X :int ,Y :int", {"args": "X, Y", "type": "Tuple[int, int]"}),
                ("X:int,Y : int", {"args": "X, Y", "type": "Tuple[int, int]"}),
                ("x: int, y: int", {"args": "X, Y", "type": "Tuple[int, int]"}),
                ("X: int,", {"args": "X", "type": "Tuple[int]"}),
                (
                    "X: int, Y: int, Z: int",
                    {"args": "X, Y, Z", "type": "Tuple[int, int, int]"},
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: Parser, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_数値型リストを解析する:
            cases = [
                ("X: List[int]", {"args": "X", "type": "List[int]"}),
                ("x: List[ int ]", {"args": "X", "type": "List[int]"}),
                ("X: List [int]", {"args": "X", "type": "List[int]"}),
                ("X: List [  int ]", {"args": "X", "type": "List[int]"}),
                ("X: list[int]", {"args": "X", "type": "List[int]"}),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: Parser, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_文字列型を解析する:
            cases = [
                ("X: str", {"args": "X", "type": "str"}),
                ("x: str", {"args": "X", "type": "str"}),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: Parser, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_文字列型タプルを解析する:
            cases = [
                ("X: str, Y: str", {"args": "X, Y", "type": "Tuple[str, str]"}),
                ("x: str, y: str", {"args": "X, Y", "type": "Tuple[str, str]"}),
                ("X: str,", {"args": "X", "type": "Tuple[str]"}),
                (
                    "X: str, Y: str, Z: str",
                    {"args": "X, Y, Z", "type": "Tuple[str, str, str]"},
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: Parser, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_文字列型リストを解析する:
            cases = [
                ("X: List[str]", {"args": "X", "type": "List[str]"}),
                ("X: list[str]", {"args": "X", "type": "List[str]"}),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: Parser, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_タプル型リストを解析する:
            cases = [
                (
                    "X: List[A: int, B: int]",
                    {"args": "X", "type": "List[Tuple[int, int]]"},
                ),
                (
                    "X: List [ A : int , B : int ]",
                    {"args": "X", "type": "List[Tuple[int, int]]"},
                ),
                (
                    "X: list[a: int, b: int]]",
                    {"args": "X", "type": "List[Tuple[int, int]]"},
                ),
                (
                    "X: list[a: int, b: int, c: int]]",
                    {"args": "X", "type": "List[Tuple[int, int, int]]"},
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: Parser, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_異なる型のタプルを解析する:
            cases = [
                "X: int, Y: str",
                "X: str, Y: int",
            ]

            @pytest.mark.parametrize("args", cases, ids=ids_raise_ValueError(cases))
            def test(self, parser: Parser, args):
                with pytest.raises(ValueError):
                    parser.parse(args)

        class Test_対応していない型を解析する:
            cases = [
                "X: number",
                "X: Tuple[A: int]",
                "X: Tuple[A: int, B: int]",
            ]

            @pytest.mark.parametrize("args", cases, ids=ids_raise_ValueError(cases))
            def test(self, parser: Parser, args):
                with pytest.raises(ValueError):
                    parser.parse(args)

        class Test_入力に不備があるものを解析する:
            cases = [
                "X",
                "X: List[int",
                "X: List[number]",
                "Y: ListA: lint,",
                "X, Y: [int, int]",
                "X Y: int",
                "X: int int",
                "X: int, int",
            ]

            @pytest.mark.parametrize("args", cases, ids=ids_raise_ValueError(cases))
            def test(self, parser: Parser, args):
                with pytest.raises(ValueError):
                    print(parser.parse(args))
