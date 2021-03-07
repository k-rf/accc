import pytest
from accc.core.domain.test_code.parsed_data import ParsedData
from accc.core.domain.test_code.test_code_service import TestCodeService


@pytest.fixture
def parser():
    return TestCodeService()


class Test_テストコード用の文字列を解析するTestCodeServiceクラス:
    class Test_文字列を解析してParsedData型に変換するparseメソッド:
        def test_単一の解析する(self, parser: TestCodeService):
            args = [
                "3",
                "1 2 3",
                "4 5 6",
                "7 8 9",
            ]
            expected = ParsedData(args, "45")

            assert parser.parse((args, "45")) == expected

        def test_複数の解析する(self, parser: TestCodeService):
            args = [
                "3",
                "1 2 3",
                "4 5 6",
                "7 8 9",
            ]
            expected = [
                ParsedData(args, "45"),
                ParsedData(args, "362880"),
            ]

            assert parser.parse([(args, "45"), (args, "362880")]) == expected
