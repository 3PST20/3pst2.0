# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../3pst2.0/pst2/resourcesProjeto'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '3PST_2.0.0'
copyright = '2024, INPE/COGPI/SEPEC'
author = 'INPE/COGPI/SEPEC'
release = '2.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_js']

#extensions = ["sphinx.ext.autodoc"]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# todo_include_todos = True

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Diretório do códigos em JavaScript 2024 -----------------

js_source_path = 'C:\\Users\\ere_m\\OneDrive\\Documentos\\GitHub\\3pst2.0\\pst2\\static\\js'



