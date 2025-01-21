# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pipmake'
copyright = '2025, Kendrick Smith'
author = 'Kendrick Smith'

import pipmake

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html
extensions = ['sphinx.ext.autosectionlabel']
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
extensions += ['sphinx.ext.autosummary', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon']

autoclass_content = 'both'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_theme_options = {
    'body_max_width' : 'none',
    'page_width': 'auto',
}
