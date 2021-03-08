from accc.core.usecase.test_code.test_code_input_data import TestCodeInputData
from accc.core.usecase.test_code.test_code_usecase import TestCodeUsecase
from injector import inject


class TestCodeController:
    @inject
    def __init__(self, usecase: TestCodeUsecase):
        self.__usecase = usecase

    def create_test_code(
        self,
        test_code_name: str,
        product_code_name: str,
        raw_data: list[tuple[list[str], str]],
    ):
        input_data = TestCodeInputData(
            test_code_name,
            product_code_name,
            raw_data,
        )
        self.__usecase.create(input_data)
