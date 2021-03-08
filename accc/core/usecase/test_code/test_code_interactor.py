from accc.core.domain.product_code.file_name import FileName
from accc.core.domain.test_code.test_code import TestCode
from accc.core.domain.test_code.test_code_service import TestCodeService
from accc.core.usecase.test_code.test_code_input_data import TestCodeInputData
from accc.core.usecase.test_code.test_code_output_data import TestCodeOutputData
from accc.core.usecase.test_code.test_code_presenter import TestCodePresenter
from accc.core.usecase.test_code.test_code_usecase import TestCodeUsecase
from injector import inject


class TestCodeInteractor(TestCodeUsecase):
    @inject
    def __init__(self, presenter: TestCodePresenter):
        self.__service = TestCodeService()
        self.__presenter = presenter

    def create(self, input_data: TestCodeInputData):
        parsed_data = self.__service.parse(input_data.raw_data)

        code = TestCode(FileName(input_data.file_name), parsed_data)

        data = TestCodeOutputData(
            code.file_name.with_ext, [str(x) for x in code.readables]
        )

        self.__presenter.output(data)
