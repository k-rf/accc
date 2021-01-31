from dataclasses import asdict

import pytest
from accc.core.domain.product_code.file_name import FileName
from accc.core.domain.product_code.input_part import InputPart
from accc.core.domain.product_code.product_code import ProductCode
from accc.core.domain.product_code.product_code_service import \
    ProductCodeService


class Test_プロダクトコードを扱うProductCodeクラス:
    # TODO: なんてテストすれば良いんだ？
    def test_インスタンス化する(self):
        service = ProductCodeService()
        parsed_data = service.parse(
            [
                "N: int",
                "A: int, B: int",
                "X: list[int]",
                "Y: list[A: int, B: int, C: int]]",
            ]
        )
        ProductCode(FileName("a"), parsed_data)
