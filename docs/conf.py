# docs/conf.py
"""Sphinx configuration."""
from datetime import datetime
import sphinx_rtd_theme

project = "remindo-api"
author = "Leonardo Vida"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
]
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    #'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
html_context = {
    'theme_vcs_pageview_mode': 'edit'
}