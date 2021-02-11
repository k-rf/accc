from accc.core.usecase.product_code.product_code_input_data import ProductCodeInputData
from accc.core.usecase.product_code.product_code_interactor import ProductCodeInteractor
from tests.core.usecase.product_code.mock_product_code_presenter import (
    MockProductCodePresenter,
)


class Test_プロダクトコード用のインタラクタクラス:
    class Test_プロダクトコードを生成するcreateメソッド:
        def test_解析可能な文字列を受け取る(self, tmp_path):
            presenter = MockProductCodePresenter(tmp_path)
            interactor = ProductCodeInteractor(presenter)

            input_data = ProductCodeInputData("hoge.py", ["N: int, M: int", "X: str"])
            interactor.create(input_data)

            with open(tmp_path / "hoge.py", "r") as f:
                assert f.readlines() == [
                    "N, M\n",
                    "X\n",
                    "\n",
                    "N, M = [int(x) for x in input().split()]\n",
                    "X = input()\n",
                    "N: int, M: int\n",
                    "X: str",
                ]
