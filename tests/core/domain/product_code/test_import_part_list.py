from typing import List, Tuple
import pytest
from accc.core.domain.product_code.import_part import ImportPart
from accc.core.domain.product_code.import_part_list import ImportPartList
from accc.core.domain.product_code.parsed_data import ParsedData


def ids(value: List[Tuple[List[ParsedData], ParsedData]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


class Test_ImportPartのリストクラス:
    class Test_初期化時にimport形式のリストに変換する:
        cases = [
            (
                [
                    ParsedData("Y", "List[Tuple[int, int, int]]"),
                    ParsedData("X", "List[int]"),
                    ParsedData("A, B", "Tuple[int, int]"),
                    ParsedData("N", "int"),
                ],
                ParsedData("Y", "List[Tuple[int, int, int]]"),
            ),
            (
                [
                    ParsedData("N", "int"),
                    ParsedData("A, B", "Tuple[int, int]"),
                    ParsedData("X", "List[int]"),
                    ParsedData("Y", "List[Tuple[int, int, int]]"),
                ],
                ParsedData("Y", "List[Tuple[int, int, int]]"),
            ),
            (
                [
                    ParsedData("Y", "List[Tuple[int, int, int]]"),
                ],
                ParsedData("Y", "List[Tuple[int, int, int]]"),
            ),
            (
                [
                    ParsedData("X", "List[int]"),
                ],
                ParsedData("X", "List[int]"),
            ),
        ]

        @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
        def test_パース後の配列形式データを変換する(self, args, expected):
            list = ImportPartList(args)

            assert len(list) == 1
            for actual in list:
                assert actual == ImportPart(expected)
