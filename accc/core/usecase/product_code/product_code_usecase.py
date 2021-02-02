from abc import ABC, abstractclassmethod

from accc.core.usecase.product_code.product_code_input_data import ProductCodeInputData


class ProductCodeUsecase(ABC):
    @abstractclassmethod
    def create(self, input_data: ProductCodeInputData):
        ...
