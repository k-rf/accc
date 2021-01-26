from accc.core.domain.product_code.input_part import InputPart
from accc.core.domain.product_code.parsed_data import ParsedData
from accc.core.domain.product_code.input_part_list import InputPartList


class Test_InputPartのリストクラス:
    class Test_初期化時に入力形式のリストに変換する:
        def test_パース後の配列形式データを変換する(self):
            parsed_data = [
                ParsedData("N", "int"),
                ParsedData("A, B", "Tuple[int, int]"),
                ParsedData("X", "List[int]"),
                ParsedData("Y", "List[Tuple[int, int, int]]"),
            ]

            list = InputPartList(parsed_data)

            assert len(list) == 4
            for actual, expected in zip(list, parsed_data):
                assert actual == InputPart(expected)
