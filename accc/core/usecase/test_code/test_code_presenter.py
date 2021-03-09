from abc import ABC, abstractclassmethod

from accc.core.usecase.test_code.test_code_output_data import TestCodeOutputData


class TestCodePresenter(ABC):
    @abstractclassmethod
    def output(self, output_data: TestCodeOutputData):
        ...
