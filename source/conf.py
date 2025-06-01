# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FRC30DayIronMan'
copyright = '2025, Justmore5mins'
author = 'Justmore5mins'
release = '2025.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
    'sphinxawesome_theme',
    'sphinx_design'
]

templates_path = ['_templates']
exclude_patterns = []


html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
pygments_style = 'xcode'
pygments_style_dark = 'lightbulb'
html_title = "FRC 30天鐵人賽"
html_static_path = ['_static']