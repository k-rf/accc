from typing import List
from accc.core.domain.product_code.file_name import FileName
from dataclasses import InitVar, dataclass, field

from accc.core.domain.product_code.argument_part_list import ArgumentPartList
from accc.core.domain.product_code.import_part_list import ImportPartList
from accc.core.domain.product_code.input_part_list import InputPartList
from accc.core.domain.product_code.parameter_part_list import ParameterPartList
from accc.core.domain.product_code.parsed_data import ParsedData


@dataclass
class ProductCode:
    file_name: FileName
    parsed_data: InitVar[List[ParsedData]]
    import_parts: ImportPartList = field(init=False)
    parameter_parts: ParameterPartList = field(init=False)
    input_parts: InputPartList = field(init=False)
    argument_parts: ArgumentPartList = field(init=False)

    def __post_init__(self, parsed_data: List[ParsedData]):
        self.import_parts = ImportPartList(parsed_data)
        self.parameter_parts = ParameterPartList(parsed_data)
        self.input_parts = InputPartList(parsed_data)
        self.argument_parts = ArgumentPartList(parsed_data)
