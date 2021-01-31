import pytest
from accc.core.domain.product_code.file_name import FileName


def ids(value: list[tuple[str, str]]):
    return (f"{x[0]} >> {x[1]}" for x in value)


class Test_プロダクトコードのファイル名を扱うFileNameクラス:
    class Test_初期化処理:
        def test_空文字を与えるとエラーになる(self):
            with pytest.raises(ValueError) as excinfo:
                FileName("")

            assert str(excinfo.value) == "Empty string is not supported."

        def test_空白相当の文字列のみを与えるとエラーになる(self):
            with pytest.raises(ValueError) as excinfo:
                FileName("    ")

            assert str(excinfo.value) == "Empty string is not supported."

        cases = [("a.py", "a"), ("a.ts", "a.ts")]

        @pytest.mark.parametrize(("args", "expected"), cases, ids=ids(cases))
        def test_拡張子がpyのときは取り除く(self, args, expected):
            assert str(FileName(args)) == expected
