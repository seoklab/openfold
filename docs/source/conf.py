# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re

from sphinx.ext import autodoc

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "OpenFold"
copyright = "2024, OpenFold Team"
author = "OpenFold Team"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]

autodoc_member_order = "groupwise"
autodoc_typehints = "description"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "ignore-module-all": True,
}
autodoc_inherit_docstrings = False

autosummary_generate = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "torch": ("https://pytorch.org/docs/stable", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "Bio": ("https://biopython.org/docs/latest", None),
}

myst_enable_extensions = ["colon_fence", "dollarmath", "amsmath"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

add_module_names = False
python_display_short_literal_types = True
python_use_unqualified_type_names = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_last_updated_fmt = "%Y-%m-%d %H:%M"

html_static_path = ["_static"]


class StrippingDocumenter(autodoc.ClassDocumenter):
    _strip_re = re.compile(r"\s*Bases:\s*:py:class:`(object)`\s*")

    def add_line(self, line: str, source: str, *lineno: int):
        if self._strip_re.fullmatch(line):
            return
        super().add_line(line, source, *lineno)


autodoc.ClassDocumenter = StrippingDocumenter  # type: ignore
