from accc.core.usecase.test_code.test_code_input_data import TestCodeInputData
from accc.core.usecase.test_code.test_code_interactor import TestCodeInteractor
from accc import interface
from tests.core.usecase.test_code.mock_test_code_presenter import MockTestCodePresenter


class Test_テストコード用のインタラクタクラス:
    class Test_テストコードを生成するcreateメソッド:
        def test_Mock解析可能な文字列を受け取る(self, tmp_path):
            presenter = MockTestCodePresenter(tmp_path)
            interactor = TestCodeInteractor(presenter)

            file_name = "test_code_file"
            output_file_name = file_name + ".py"
            input_data = TestCodeInputData(
                file_name,
                [
                    (["2", "1 2 3", "4 5 6"], "21"),
                    (["3", "1 2 3", "4 5 6", "7 8 9"], "45"),
                ],
            )
            interactor.create(input_data)

            with open(tmp_path / output_file_name, "r") as f:
                assert f.read() == "".join(
                    ["2\n1 2 3\n4 5 6\n\n21\n", "3\n1 2 3\n4 5 6\n7 8 9\n\n45\n"]
                )
