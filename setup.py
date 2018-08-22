#!/usr/bin/env python3
#
# The purpose of this script is to enable uploading xdot.py to the Python
# Package Index, which can be easily done by doing:
#
#   python3 setup.py sdist upload
#
# See also:
# - https://packaging.python.org/distributing/
# - https://docs.python.org/3/distutils/packageindex.html
#

from setuptools import setup

setup(
    name='xdot',
    version='0.92',
    author='Jose Fonseca, Mathias Kreider',
    author_email='jose.r.fonseca@gmail.com, m.kreider@gsi.de',
    url='https://github.com/jrfonseca/xdot.py',
    description="Interactive viewer for Graphviz dot files",
    long_description="""
        Fork of xdot viewer. Original bei Jose Fonseca, forked by Mathias Kreider
        Aug 2018 @ GSI Darmstadt.

        Changes:
        - Enforcing minimum linewidth when zooming so objects don't disappear
        - Added inspection window for bundled node and edge properties
	- Added regex search support to bundled properties if inspection is turned on
        - Added ability to pass arguments to filter (dot, neato, etc) from CLI
        - Added zoom animation to bounding box of nodes in search result
        - various bug fixes
        - Added GSI DM schedule specific filter to inspection of bundled properties
 
	
        Original description:
        xdot.py is an interactive viewer for graphs written in Graphviz's dot
        language.

        It uses internally the graphviz's xdot output format as an intermediate
        format, and PyGTK and Cairo for rendering.

        xdot.py can be used either as a standalone application from command
        line, or as a library embedded in your python application.
        """,
    license="LGPL",

    packages=['xdot', 'xdot/dot', 'xdot/ui', 'xdot/gsi'],
    entry_points=dict(gui_scripts=['xdot=xdot.__main__:main']),

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 6 - Mature',

        'Environment :: X11 Applications :: GTK',

        'Intended Audience :: Information Technology',

        'Operating System :: OS Independent',

        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',

        'Topic :: Multimedia :: Graphics :: Viewers',
    ],

    # This is true, but doesn't work realiably
    #install_requires=['gi', 'gi-cairo'],
)
