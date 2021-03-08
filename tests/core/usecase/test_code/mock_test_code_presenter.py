from accc.core.usecase.test_code.test_code_output_data import TestCodeOutputData
from accc.core.usecase.test_code.test_code_presenter import TestCodePresenter
from pathlib import Path


class MockTestCodePresenter(TestCodePresenter):
    def __init__(self, path: Path):
        self.path = path

    def output(self, output_data: TestCodeOutputData):
        with open(self.path / output_data.file_name, "w") as f:
            for data in zip(output_data.readables, output_data.expectations):
                f.writelines("".join(data))
