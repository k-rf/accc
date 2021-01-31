from accc.core.domain.product_code.parameter_part import ParameterPart
from accc.core.domain.product_code.parameter_part_list import ParameterPartList
from accc.core.domain.product_code.parsed_data import ParsedData


class Test_ParameterPartのリストクラス:
    class Test_初期化時にパラメータ形式のリストに変換する:
        def test_パース後の配列形式データを変換する(self):
            parsed_data = [
                ParsedData("N", "int"),
                ParsedData("A, B", "Tuple[int, int]"),
                ParsedData("X", "List[int]"),
                ParsedData("Y", "List[Tuple[int, int, int]]"),
            ]

            list = ParameterPartList(parsed_data)

            assert len(list) == 4
            for actual, expected in zip(list, parsed_data):
                assert actual == ParameterPart(expected)
