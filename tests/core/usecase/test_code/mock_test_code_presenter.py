from accc.core.usecase.test_code.test_code_output_data import TestCodeOutputData
from accc.core.usecase.test_code.test_code_presenter import TestCodePresenter
from pathlib import Path


class MockTestCodePresenter(TestCodePresenter):
    def __init__(self, path: Path):
        self.path = path

    def output(self, output_data: TestCodeOutputData):
        with open(self.path / output_data.file_name, "w") as f:
            f.writelines(output_data.readables)
