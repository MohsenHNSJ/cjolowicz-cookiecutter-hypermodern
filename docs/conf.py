"""Sphinx configuration."""

project = "Cjolowicz Cookiecutter Hypermodern"
author = "Mohsen Hasan Nezhad"
copyright = "2025, Mohsen Hasan Nezhad"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
