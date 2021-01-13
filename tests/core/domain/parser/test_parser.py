from typing import Tuple
import pytest
from accc.core.domain.parser.parser import Parser


class Test_文字列を解析するParserクラス:
    class Test_parseメソッドは文字列を解析して辞書型に変換する:
        @pytest.fixture
        def parser(self):
            return Parser()

        class Test_数値型を解析する:
            cases = [
                ("X: int", {"args": "X", "type": "int"}),
                ("x: int", {"args": "X", "type": "int"}),
                ("X:int", {"args": "X", "type": "int"}),
                ("X :int", {"args": "X", "type": "int"}),
                ("X : int", {"args": "X", "type": "int"}),
            ]

            @pytest.mark.parametrize(
                ("args", "expected"), cases, ids=[f"{x[0]} >> {x[1]}" for x in cases]
            )
            def test_解析する(self, parser: Parser, args, expected):
                assert parser.parse(args) == expected

        class Test_数値型タプルを解析する:
            cases = [
                ("X: int, Y: int", {"args": "X, Y", "type": "Tuple[int, int]"}),
                ("x: int, y: int", {"args": "X, Y", "type": "Tuple[int, int]"}),
                ("X: int,", {"args": "X", "type": "Tuple[int]"}),
                (
                    "X: int, Y: int, Z: int",
                    {"args": "X, Y, Z", "type": "Tuple[int, int, int]"},
                ),
            ]

            @pytest.mark.parametrize(
                ("args", "expected"), cases, ids=[f"{x[0]} >> {x[1]}" for x in cases]
            )
            def test_解析する(self, parser: Parser, args, expected):
                assert parser.parse(args) == expected

        class Test_文字列型を解析する:
            cases = [
                ("X: str", {"args": "X", "type": "str"}),
                ("x: str", {"args": "X", "type": "str"}),
            ]

            @pytest.mark.parametrize(
                ("args", "expected"), cases, ids=[f"{x[0]} >> {x[1]}" for x in cases]
            )
            def test_解析する(self, parser: Parser, args, expected):
                assert parser.parse(args) == expected

        class Test_文字列型タプルを解析する:
            cases = [
                ("X: str, Y: str", {"args": "X, Y", "type": "Tuple[str, str]"}),
                ("x: str, y: str", {"args": "X, Y", "type": "Tuple[str, str]"}),
            ]

            @pytest.mark.parametrize(
                ("args", "expected"), cases, ids=[f"{x[0]} >> {x[1]}" for x in cases]
            )
            def test_解析する(self, parser: Parser, args, expected):
                assert parser.parse(args) == expected

        class Test_異なる型のタプルを解析する:
            cases = [
                ("X: int, Y: str"),
                ("X: str, Y: int"),
            ]

            @pytest.mark.parametrize(
                "args", cases, ids=[f"{x} >> raise ValueError" for x in cases]
            )
            def test_解析する(self, parser: Parser, args):
                with pytest.raises(ValueError):
                    parser.parse(args)
