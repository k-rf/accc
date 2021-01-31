from abc import ABC

from accc.core.domain.product_code.product_code import ProductCode


class ProductCodeRepository(ABC):
    def save(self, code: ProductCode):
        ...
