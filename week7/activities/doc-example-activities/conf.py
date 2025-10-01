# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import os
import sys
sys.path.insert(0, os.path.abspath('../src'))


project = 'Sphinx tutorial - tac_tac_bug_toe - task_bug'
copyright = '2025, Marcos Castilho'
author = 'Marcos Castilho'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx.ext.mathjax', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon']

napoleon_google_docstring = False
napoleon_numpy_docstring = True

autodoc2_packages = [
    {
        "path": "src",
        "module": "tac_tac_bug_toe",
    },
    {
        "path": "src",
        "module": "task_bug",
    }
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'groundwork'
html_static_path = ['_static']
