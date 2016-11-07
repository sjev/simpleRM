#!/usr/bin/env python

"""Setup script for simpleRM """

import setuptools

from simpleRM import __project__, __version__, CLI, DESCRIPTION


setuptools.setup(
    name=__project__,
    version=__version__,

    description=DESCRIPTION,
    url='https://sjev.github.io/simpleRM/',
    author='Jev Kuznetsov',
    author_email='jev.kuznetsov@gmail.com',

    packages=setuptools.find_packages(),
    #package_data={'doorstop.core': ['files/*']},

    entry_points={
        'console_scripts': [CLI + ' = simpleRM.main:main']
    },

    
    license='LGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Editors :: Documentation',
        'Topic :: Text Processing :: Markup',
    ],

    install_requires=[
        "PyYAML >= 3.10, < 4",
        "Markdown >= 2, < 3",
        "bottle >= 0.12, < 0.13",
        "mkdocs >= 0.15"
    ],
)
