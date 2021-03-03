from accc.core.usecase.product_code.product_code_input_data import ProductCodeInputData
from accc.core.usecase.product_code.product_code_usecase import ProductCodeUsecase
from injector import inject


class ProductCodeController:
    @inject
    def __init__(self, usecase: ProductCodeUsecase):
        self.__usecase = usecase

    def create_product_code(self, file_name: str, raw_data: list[str]):
        input_data = ProductCodeInputData(file_name, raw_data)
        self.__usecase.create(input_data)
