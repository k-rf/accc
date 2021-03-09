import os
from pathlib import Path

from accc.__main__ import app
from typer.testing import CliRunner

runner = CliRunner()


class Test_メインコンポーネント:
    def test_コマンド(self, tmpdir):
        os.chdir(tmpdir)
        result = runner.invoke(
            app,
            ["a"],
            "".join(
                [
                    # product code
                    "n: int\n",
                    "x: List[a: int, b: int, c: int]\n",
                    "\n",
                    # test code
                    "3\n1 2 3\n4 5 6\n7 8 9\n",
                    "\n",
                    "45\n",
                    "\n",
                ]
            ),
        )
        assert result.exit_code == 0
        assert Path(tmpdir / "a.py").is_file()
        assert Path(tmpdir / "test_a.py").is_file()
