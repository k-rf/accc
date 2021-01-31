from dataclasses import asdict
from accc.core.domain.product_code.product_code import ProductCode
from accc.core.domain.product_code.product_code_repository import ProductCodeRepository
from jinja2 import Environment, FileSystemLoader, Template
from pathlib import Path


class FileProductCodeRepository(ProductCodeRepository):
    def __init__(self, path: Path):
        self.path = path

    def save(self, code: ProductCode):
        env = Environment(loader=FileSystemLoader(self.path, encoding="utf-8"))
        template = env.get_template("product_code.j2")

        rendered = template.render(asdict(code))

        print(rendered)
