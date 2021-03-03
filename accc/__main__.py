from pathlib import Path

import typer
from injector import Binder, Injector

from accc.core.usecase.product_code.product_code_interactor import ProductCodeInteractor
from accc.core.usecase.product_code.product_code_presenter import (
    ProductCodePresenter as IProductCodePresenter,
)
from accc.core.usecase.product_code.product_code_usecase import ProductCodeUsecase
from accc.interface.cli.product_code.product_code_controller import (
    ProductCodeController,
)
from accc.interface.cli.product_code.product_code_presenter import ProductCodePresenter


def configure(binder: Binder):
    cwd = Path.cwd()

    # usecase
    binder.bind(interface=ProductCodeUsecase, to=ProductCodeInteractor)
    binder.bind(ProductCodeInteractor)

    # presenter
    binder.bind(interface=IProductCodePresenter, to=ProductCodePresenter)
    binder.bind(ProductCodePresenter, to=cwd)

    # controller
    binder.bind(ProductCodeController)


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

    return s, "test_" + s


@app.command()
def command_gateway(file_name: str):
    product_file, test_file = check_file_existence(file_name)

    product_raw_data: list[str] = []
    while (s := input(">>> ")) != "":
        product_raw_data.append(s)

    try:
        injector.get(ProductCodeController).create_product_code(
            file_name, product_raw_data
        )
        typer.echo(f"{success}: `{product_file}` is created.")
    except Exception as e:
        typer.echo(f"{failure}: {e}", err=True)
        raise typer.Exit(1)

    test_raw_data: list[str] = []
    while (s := input(">>> ")) != "":
        test_raw_data.append(s)

    try:
        # TODO: テストコード生成処理
        typer.echo(f"{success}: `{test_file}` is created.")
    except Exception as e:
        typer.echo(f"{failure}: {e}", err=True)
        raise typer.Exit(1)


def main():
    app()


if __name__ == "__main__":
    main()
