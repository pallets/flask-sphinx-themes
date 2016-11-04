#!/usr/bin/env python
import os
import re

from setuptools import setup

with open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with open(os.path.join('flask_sphinx_themes', '__init__.py'), 'rt', encoding='utf8') as f:
    version = re.search(r'^__version__ = \'(\d+\.(?:\d+\.)*\d+)\'', f.read(), re.M).group(1)

setup(
    name='Flask-Sphinx-Themes',
    version=version,
    description='Sphinx themes for Flask and related projects.',
    long_description=readme,
    url='https://github.com/pallets/flask-sphinx-themes',
    author='Armin Ronacher',
    author_email='armin@ronacher.eu',
    maintainer='David Lord',
    maintainer_email='davidism@gmail.com',
    packages=['flask_sphinx_themes'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Sphinx'],
    entry_points={
        'sphinx_themes': [
            'path = flask_sphinx_themes:get_path',
        ],
    },
    license='BSD',
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ],
)
