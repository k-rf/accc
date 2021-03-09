from typing import List, Tuple
import pytest
from accc.core.domain.test_code.readable import Readable
from accc.core.domain.test_code.parsed_data import ParsedData


def ids(value: List[Tuple[ParsedData, str]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


class Test_テストコードの入力値部分を扱うReadableクラス:
    class Test_初期化時にreadable形式に変換する:
        cases = [(ParsedData(["2", "1 2 3", "4 5 6"], "21"), "2\\n1 2 3\\n4 5 6\\n\\n")]

        @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
        def test(self, args, expected):
            assert str(Readable(args)) == expected
