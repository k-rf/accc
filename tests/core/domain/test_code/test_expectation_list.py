from accc.core.domain.test_code.expectation import Expectation
from accc.core.domain.test_code.expectation_list import ExpectationList
from accc.core.domain.test_code.parsed_data import ParsedData


class Test_Expectationのリストクラス:
    class Test_初期化時に期待する値形式のリストに変換する:
        def test_パース後の配列形式のデータを変換する(self):
            parsed_data = [
                ParsedData(["2", "1 2 3", "4 5 6"], "21"),
                ParsedData(["3", "1 2 3", "4 5 6", "7 8 9"], "45"),
            ]

            _list = ExpectationList(parsed_data)

            assert len(_list) == 2
            for actual, expected in zip(_list, parsed_data):
                assert actual == Expectation(expected)
