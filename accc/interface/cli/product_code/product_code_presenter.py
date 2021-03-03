from dataclasses import asdict
from pathlib import Path

from accc.core.usecase.product_code.product_code_output_data import (
    ProductCodeOutputData,
)
from accc.core.usecase.product_code.product_code_presenter import (
    ProductCodePresenter as IProductCodePresenter,
)
from black import Mode, format_file_contents
from injector import inject
from jinja2 import Environment, FileSystemLoader


class ProductCodePresenter(IProductCodePresenter):
    @inject
    def __init__(self, path: Path):
        self.path = path

    def output(self, value: ProductCodeOutputData):
        env = Environment(
            loader=FileSystemLoader(Path(__file__).parent, encoding="utf-8")
        )
        template = env.get_template("product_code.j2")

        rendered = template.render(asdict(value))

        with open(self.path / value.file_name, "w") as f:
            contents = format_file_contents(rendered, fast=True, mode=Mode())
            f.write(contents)
