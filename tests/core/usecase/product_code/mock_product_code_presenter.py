from pathlib import Path

from accc.core.usecase.product_code.product_code_output_data import (
    ProductCodeOutputData,
)
from accc.core.usecase.product_code.product_code_presenter import ProductCodePresenter


class MockProductCodePresenter(ProductCodePresenter):
    def __init__(self, path: Path):
        self.path = path

    def output(self, value: ProductCodeOutputData):
        with open(self.path / value.file_name, "w") as f:
            arguments = "\n".join(value.argument_parts)
            imports = "\n".join(value.import_parts)
            inputs = "\n".join(value.input_parts)
            parameters = "\n".join(value.parameter_parts)

            f.writelines([arguments, "\n", imports, "\n", inputs, "\n", parameters])
