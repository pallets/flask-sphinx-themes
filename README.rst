Flask Sphinx Themes
===================

This repository contains Sphinx themes for Flask and Flask related
projects.  To use this theme in your Sphinx documentation:

1. Install the package using pip: `pip install Flask-Spinx-Themes`

2. Add this to ``conf.py``:

   .. code-block:: python

       html_theme = 'flask'

Themes
------

The following themes exist for ``html_theme``.

======================= ===============================================
flask                   The standard Flask documentation theme for
                        large projects

flask_small             Small single page theme.  Intended to be used
                        by very small addon libraries for Flask.
======================= ===============================================

Options
-------

The following options can be set with ``html_theme_options``.

======================= ===============================================
index_logo              Filename of a picture in ``_static`` to be used
                        as replacement for the ``h1`` in the
                        ``index.rst`` file.
                        *Default unset.*

index_logo_height       Height of the index logo.
                        *Default 120px*.

touch_icon              Filename of a picture in ``_static`` to be use
                        as the app icon on Apple devices.
                        *Default unset.*

github_fork             Repository name on GitHub for the "Fork Me"
                        badge.
                        *Default unset.*

github_ribbon_color     Color for the "Fork Me" badge.
                        *Default darkblue_121621.*
======================= ===============================================

Sidebar Templates
-----------------

The following sidebar templates can be included in ``html_sidebars``.

======================= ===============================================
relations.html          Show parent, previous, and next links.
======================= ===============================================

Pygments Style
--------------

The theme automatically sets ``pygments_style`` to the provided style.
Make sure you remove any override from ``conf.py`` or set it to
``flask_sphinx_themes.pygments.FlaskyStyle``.
