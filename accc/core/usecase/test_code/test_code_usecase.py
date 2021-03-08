from abc import ABC, abstractclassmethod

from accc.core.usecase.test_code.test_code_input_data import TestCodeInputData


class TestCodeUsecase(ABC):
    @abstractclassmethod
    def create(self, input_data: TestCodeInputData):
        ...
