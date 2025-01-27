"""Test cases for the __main__ module."""

import pytest
from click.testing import CliRunner

from cjolowicz_cookiecutter_hypermodern import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(input_runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = input_runner.invoke(__main__.main)
    assert result.exit_code == 0
