from accc.core.usecase.product_code.product_code_input_data import ProductCodeInputData
from accc.core.usecase.product_code.product_code_interactor import ProductCodeInteractor
from accc.interface.cli.product_code.product_code_presenter import ProductCodePresenter
from tests.core.usecase.product_code.mock_product_code_presenter import (
    MockProductCodePresenter,
)


class Test_プロダクトコード用のインタラクタクラス:
    class Test_プロダクトコードを生成するcreateメソッド:
        def test_Mock解析可能な文字列を受け取る(self, tmp_path):
            presenter = MockProductCodePresenter(tmp_path)
            interactor = ProductCodeInteractor(presenter)

            file_name = "product_code_file"
            output_file_name = file_name + ".py"
            input_data = ProductCodeInputData(file_name, ["N: int, M: int", "X: str"])
            interactor.create(input_data)

            with open(tmp_path / output_file_name, "r") as f:
                assert f.readlines() == [
                    "N, M\n",
                    "X\n",
                    "\n",
                    "N, M = [int(x) for x in input().split()]\n",
                    "X = input()\n",
                    "N: int, M: int\n",
                    "X: str",
                ]

        def test_解析可能な文字列を受け取る(self, tmp_path):
            presenter = ProductCodePresenter(tmp_path)
            interactor = ProductCodeInteractor(presenter)

            file_name = "product_code_file"
            output_file_name = file_name + ".py"
            input_data = ProductCodeInputData(file_name, ["N: int, M: int", "X: str"])
            interactor.create(input_data)

            with open(tmp_path / output_file_name, "r") as f:
                assert f.readlines() == [
                    "def algorithm(N: int, M: int, X: str):\n",
                    "    return -1\n",
                    "\n",
                    "\n",
                    "def main():\n",
                    "    N, M = [int(x) for x in input().split()]\n",
                    "    X = input()\n",
                    "\n",
                    "    print(algorithm(N, M, X))\n",
                    "\n",
                    "\n",
                    'if __name__ == "__main__":\n',
                    "    main()\n",
                ]
