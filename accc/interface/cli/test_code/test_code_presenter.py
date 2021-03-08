from pathlib import Path

from accc.core.usecase.test_code.test_code_output_data import TestCodeOutputData
from accc.core.usecase.test_code.test_code_presenter import (
    TestCodePresenter as ITestCodePresenter,
)
from black import Mode, format_file_contents
from injector import inject
from jinja2 import Environment, FileSystemLoader


class TestCodePresenter(ITestCodePresenter):
    @inject
    def __init__(self, path: Path):
        self.path = path

    def output(self, value: TestCodeOutputData):
        env = Environment(
            loader=FileSystemLoader(Path(__file__).parent, encoding="utf-8")
        )
        template = env.get_template("test_code.j2")

        rendered = template.render(
            {
                "parent_dir": str(Path.cwd()).split("/")[-1],
                "product_code_name": value.product_code_name,
                "data": zip(value.readables, value.expectations),
            }
        )

        with open(self.path / value.file_name, "w") as f:
            contents = format_file_contents(rendered, fast=True, mode=Mode())
            f.write(contents)
