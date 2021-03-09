import pytest
from accc.core.domain.test_code.expectation import Expectation
from accc.core.domain.test_code.parsed_data import ParsedData


def ids(value: list[tuple[ParsedData, str]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


class Test_テストコードの期待する値を扱うExpectationクラス:
    class Test_初期化時に期待する値形式に変換する:
        cases = [(ParsedData(["2", "1 2 3", "4 5 6"], "21"), "21")]

        @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
        def test(self, args, expected):
            assert str(Expectation(args)) == expected
