from pathlib import Path
from typing import List, Tuple

import typer
from injector import Binder, Injector

from accc.core.usecase.product_code.product_code_interactor import ProductCodeInteractor
from accc.core.usecase.product_code.product_code_presenter import (
    ProductCodePresenter as IProductCodePresenter,
)
from accc.core.usecase.product_code.product_code_usecase import ProductCodeUsecase
from accc.core.usecase.test_code.test_code_interactor import TestCodeInteractor
from accc.core.usecase.test_code.test_code_presenter import (
    TestCodePresenter as ITestCodePresenter,
)
from accc.core.usecase.test_code.test_code_usecase import TestCodeUsecase
from accc.interface.cli.product_code.product_code_controller import (
    ProductCodeController,
)
from accc.interface.cli.product_code.product_code_presenter import ProductCodePresenter
from accc.interface.cli.test_code.test_code_controller import TestCodeController
from accc.interface.cli.test_code.test_code_presenter import TestCodePresenter


def configure(binder: Binder):
    cwd = Path.cwd()

    # usecase
    binder.bind(interface=ProductCodeUsecase, to=ProductCodeInteractor)
    binder.bind(interface=TestCodeUsecase, to=TestCodeInteractor)
    binder.bind(ProductCodeInteractor)
    binder.bind(TestCodeInteractor)

    # presenter
    binder.bind(interface=IProductCodePresenter, to=ProductCodePresenter)
    binder.bind(interface=ITestCodePresenter, to=TestCodePresenter)
    binder.bind(ProductCodePresenter, to=cwd)
    binder.bind(TestCodePresenter, to=cwd)

    # controller
    binder.bind(ProductCodeController)
    binder.bind(TestCodeController)


injector = Injector(modules=[configure])
app = typer.Typer(add_completion=False)

success = typer.style("Success", fg=typer.colors.GREEN, bold=True)
failure = typer.style("Failure", fg=typer.colors.WHITE, bg=typer.colors.RED)


def check_file_existence(s: str):
    if not s.endswith(".py"):
        s += ".py"

    if Path(Path.cwd() / s).is_file():
        typer.echo(f"{failure}: `{s}` is existed.", err=True)
        raise typer.Exit(1)

    return s, f"test_{str(Path.cwd()).split('/')[-1]}_{s}"


@app.command()
def command_gateway(file_name: str):
    product_file, test_file = check_file_existence(file_name)

    print("------------------------")
    print("  N: int")
    print("  A: int, B: int")
    print("  L: List[int]")
    print("  X: List[int, int]; N")
    print("------------------------")
    print("Please input data for product code.")

    product_raw_data: List[str] = []
    prompt = ">>> \n"
    while (s := input(prompt)) != "":
        product_raw_data.append(s)
        prompt = ""

    print("Please input data for test code.")

    test_raw_data: List[Tuple[List[str], str]] = []
    loop = True
    while loop:
        loop = False

        row: List[str] = []
        prompt = ">>> \n"
        while (s := input(prompt)) != "":
            loop = True
            row.append(s)
            prompt = ""

        if loop:
            expected = input("Expected Value: ")
            test_raw_data.append((row, expected))

    try:
        injector.get(ProductCodeController).create_product_code(
            file_name, product_raw_data
        )
        typer.echo(f"{success}: `{product_file}` is created.")

        injector.get(TestCodeController).create_test_code(
            test_file, product_file, test_raw_data
        )
        typer.echo(f"{success}: `{test_file}` is created.")
    except Exception as e:
        typer.echo(f"{failure}: {e}", err=True)
        raise typer.Exit(1)


def main():
    app()


if __name__ == "__main__":
    main()
