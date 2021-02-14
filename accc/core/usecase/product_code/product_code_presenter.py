from abc import ABC, abstractclassmethod
from pathlib import Path

from accc.core.usecase.product_code.product_code_output_data import (
    ProductCodeOutputData,
)


class ProductCodePresenter(ABC):
    @abstractclassmethod
    def output(self, output_data: ProductCodeOutputData):
        ...
