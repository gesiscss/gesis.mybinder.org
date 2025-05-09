# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Methods Hub's Interactive Environment's Kubernetes Cluster"
copyright = '2025, Methods Hub Team'
author = '"Methods Hub Team'
release = "YYYY.MM.DD"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # Documentation at https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html

html_baseurl = "/binder.methodshub.gesis.org/"

html_copy_source = False

html_theme_options = {
    "display_version": True,
    "prev_next_buttons_location": "both",
    "style_external_links": True,
    "vcs_pageview_mode": "blob",
}

html_context = {
    "display_gitlab": True,
    "gitlab_host": "git.gesis.org",
    "gitlab_user": "methods-hub",
    "gitlab_repo": "binder.methodshub.gesis.org",
    "gitlab_version": "main",
    "conf_py_path": "/docs/source/",
}

html_static_path = ["_static"]
