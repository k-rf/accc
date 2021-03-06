from dataclasses import asdict
from typing import Dict, List, Tuple

import pytest
from accc.core.domain.product_code.product_code_service import ProductCodeService


def ids(value: List[Tuple[str, Dict[str, str]]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


def ids_raise_ValueError(value: List[str]):
    return (f"{x} >> raise ValueError" for x in value)


@pytest.fixture
def parser():
    return ProductCodeService()


class Test_文字列を解析するProductCodeServiceクラス:
    class Test_parseメソッドは文字列を解析してParsedData型に変換する:
        class Test_数値型を解析する:
            cases = [
                ("X: int", {"args": "X", "type": "int", "option": None}),
                ("X:int", {"args": "X", "type": "int", "option": None}),
                ("X :int", {"args": "X", "type": "int", "option": None}),
                ("X : int", {"args": "X", "type": "int", "option": None}),
                ("x: int", {"args": "X", "type": "int", "option": None}),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: ProductCodeService, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_数値型タプルを解析する:
            cases = [
                (
                    "X: int, Y: int",
                    {"args": "X, Y", "type": "Tuple[int, int]", "option": None},
                ),
                (
                    "X : int , Y:int",
                    {"args": "X, Y", "type": "Tuple[int, int]", "option": None},
                ),
                (
                    "X :int ,Y :int",
                    {"args": "X, Y", "type": "Tuple[int, int]", "option": None},
                ),
                (
                    "X:int,Y : int",
                    {"args": "X, Y", "type": "Tuple[int, int]", "option": None},
                ),
                (
                    "x: int, y: int",
                    {"args": "X, Y", "type": "Tuple[int, int]", "option": None},
                ),
                ("X: int,", {"args": "X", "type": "Tuple[int]", "option": None}),
                (
                    "X: int, Y: int, Z: int",
                    {"args": "X, Y, Z", "type": "Tuple[int, int, int]", "option": None},
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: ProductCodeService, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_数値型リストを解析する:
            cases = [
                ("X: List[int]", {"args": "X", "type": "List[int]", "option": None}),
                ("x: List[ int ]", {"args": "X", "type": "List[int]", "option": None}),
                ("X: List [int]", {"args": "X", "type": "List[int]", "option": None}),
                (
                    "X: List [  int ]",
                    {"args": "X", "type": "List[int]", "option": None},
                ),
                ("X: List[int]", {"args": "X", "type": "List[int]", "option": None}),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: ProductCodeService, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_文字列型を解析する:
            cases = [
                ("X: str", {"args": "X", "type": "str", "option": None}),
                ("x: str", {"args": "X", "type": "str", "option": None}),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: ProductCodeService, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_文字列型タプルを解析する:
            cases = [
                (
                    "X: str, Y: str",
                    {"args": "X, Y", "type": "Tuple[str, str]", "option": None},
                ),
                (
                    "x: str, y: str",
                    {"args": "X, Y", "type": "Tuple[str, str]", "option": None},
                ),
                ("X: str,", {"args": "X", "type": "Tuple[str]", "option": None}),
                (
                    "X: str, Y: str, Z: str",
                    {"args": "X, Y, Z", "type": "Tuple[str, str, str]", "option": None},
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: ProductCodeService, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_文字列型リストを解析する:
            cases = [
                ("X: List[str]", {"args": "X", "type": "List[str]", "option": None}),
                ("X: List[str]", {"args": "X", "type": "List[str]", "option": None}),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: ProductCodeService, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_タプル型リストを解析する:
            cases = [
                (
                    "X: List[int, int]; N",
                    {"args": "X", "type": "List[Tuple[int, int]]", "option": "N"},
                ),
                (
                    "X: List [ int ,  int ] ;  M",
                    {"args": "X", "type": "List[Tuple[int, int]]", "option": "M"},
                ),
                (
                    "x: List[int, int, int];k",
                    {"args": "X", "type": "List[Tuple[int, int, int]]", "option": "K"},
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, parser: ProductCodeService, args, expected):
                assert asdict(parser.parse(args)) == expected

        class Test_異なる型のタプルを解析する:
            cases = [
                "X: int, Y: str",
                "X: str, Y: int",
            ]

            @pytest.mark.parametrize("args", cases, ids=ids_raise_ValueError(cases))
            def test(self, parser: ProductCodeService, args):
                with pytest.raises(ValueError):
                    parser.parse(args)

        class Test_対応していない型を解析する:
            cases = [
                "X: number",
                "X: Tuple[A: int]",
                "X: Tuple[A: int, B: int]",
            ]

            @pytest.mark.parametrize("args", cases, ids=ids_raise_ValueError(cases))
            def test(self, parser: ProductCodeService, args):
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
            def test(self, parser: ProductCodeService, args):
                with pytest.raises(ValueError):
                    print(parser.parse(args))
