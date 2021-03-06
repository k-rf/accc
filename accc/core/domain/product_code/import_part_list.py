from dataclasses import InitVar, dataclass, field
from typing import List

from accc.core.domain.product_code.import_part import ImportPart
from accc.core.domain.product_code.parsed_data import ParsedData


@dataclass
class ImportPartList:
    value: List[ImportPart] = field(default_factory=list, init=False)
    parsed_data: InitVar[List[ParsedData]]

    def __post_init__(self, parsed_data: List[ParsedData]):
        """
        >>> N: int
        >>> A: int, B: int
        >>> X: List[int]
        >>> Y: List[A: int, B: int, C: int]
        >>>
        None
        None
        from typing import List
        from sys import stdin
        from typing import List, Tuple
        """

        list_type = set()
        tuple_type = set()
        for pd in parsed_data:
            try:
                ip = ImportPart(pd)

                if "Tuple" in str(ip):
                    tuple_type.add(ip)
                elif "List" in str(ip):
                    list_type.add(ip)

            except ValueError:
                continue

        if len(tuple_type) != 0:
            self.value = list(tuple_type)
        else:
            self.value = list(list_type)

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self.value.__iter__()
