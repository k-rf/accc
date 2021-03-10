from typing import List, Tuple
import pytest
from accc.core.domain.product_code.import_part import ImportPart
from accc.core.domain.product_code.parsed_data import ParsedData


def ids(value: List[Tuple[ParsedData, str]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


class Test_プロダクトコードのimport部分を扱うImportPartクラス:
    class Test_初期化時にimport形式に変換する:
        class Test_リストのimport形式に変換する:
            cases = [
                (
                    ParsedData("X", "List[int]"),
                    "from typing import List",
                ),
                (
                    ParsedData("Y", "List[str]"),
                    "from typing import List",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ImportPart(args)) == expected

        class Test_タプル型リストのimport形式に変換する:
            cases = [
                (
                    ParsedData("X", "List[Tuple[int, int]]"),
                    "from typing import List, Tuple",
                ),
                (
                    ParsedData("Y", "List[Tuple[str, str]]"),
                    "from typing import List, Tuple",
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                assert str(ImportPart(args)) == expected

        class Test_それ以外のときエラーになる:
            cases = [
                (ParsedData("X", "int"), '"int" is not supported.'),
                (ParsedData("X", "str"), '"str" is not supported.'),
                (
                    ParsedData("X, Y", "Tuple[int, int]"),
                    '"Tuple[int, int]" is not supported.',
                ),
                (
                    ParsedData("X, Y", "Tuple[str, str]"),
                    '"Tuple[str, str]" is not supported.',
                ),
            ]

            @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
            def test(self, args, expected):
                with pytest.raises(ValueError) as excinfo:
                    ImportPart(args)
                assert str(excinfo.value) == expected
