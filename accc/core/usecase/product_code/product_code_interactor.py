from accc.core.domain.product_code.file_name import FileName
from accc.core.domain.product_code.product_code import ProductCode
from accc.core.domain.product_code.product_code_service import ProductCodeService
from accc.core.usecase.product_code.product_code_input_data import ProductCodeInputData
from accc.core.usecase.product_code.product_code_output_data import (
    ProductCodeOutputData,
)
from accc.core.usecase.product_code.product_code_presenter import ProductCodePresenter
from accc.core.usecase.product_code.product_code_usecase import ProductCodeUsecase
from injector import inject


class ProductCodeInteractor(ProductCodeUsecase):
    @inject
    def __init__(self, presenter: ProductCodePresenter):
        self.__service = ProductCodeService()
        self.__presenter = presenter

    def create(self, input_data: ProductCodeInputData):
        parsed_data = self.__service.parse(input_data.raw_data)

        code = ProductCode(FileName(input_data.file_name), parsed_data)

        data = ProductCodeOutputData(
            file_name=code.file_name.with_ext,
            import_parts=[str(x) for x in code.import_parts],
            parameter_parts=[str(x) for x in code.parameter_parts],
            input_parts=[str(x) for x in code.input_parts],
            argument_parts=[str(x) for x in code.argument_parts],
        )

        self.__presenter.output(data)
