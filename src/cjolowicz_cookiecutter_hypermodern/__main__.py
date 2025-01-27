"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Cjolowicz Cookiecutter Hypermodern."""


if __name__ == "__main__":
    main(prog_name="cjolowicz-cookiecutter-hypermodern")  # pragma: no cover
