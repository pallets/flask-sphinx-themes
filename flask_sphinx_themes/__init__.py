import os

__version__ = '1.0.2'


def setup(app):
    base = os.path.dirname(__file__)
    app.add_html_theme('flask', os.path.join(base, 'flask'))
    app.add_html_theme('flask_small', os.path.join(base, 'flask_small'))
    return {
        'version': __version__,
        'parallel_read_safe': True
    }
