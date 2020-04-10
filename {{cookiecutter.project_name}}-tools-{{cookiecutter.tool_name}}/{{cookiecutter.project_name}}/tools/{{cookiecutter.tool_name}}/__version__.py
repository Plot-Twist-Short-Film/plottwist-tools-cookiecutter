#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Version module for {{cookiecutter.project_name}}-tools-{{cookiecutter.tool_name}}
"""

from __future__ import print_function, division, absolute_import

__author__ = "{{cookiecutter.author}}"
__license__ = "MIT"
__maintainer__ = "{{cookiecutter.maintainer}}"
__email__ = "{{cookiecutter.email}}"
__version__ = None

__version__ = None


def get_version():
    from {{cookiecutter.project_name}}.tools.{{cookiecutter.tool_name}}._version import get_versions

    global __version__
    if __version__:
        return __version__
    
    __version__ = get_versions()['version']
    del get_versions

    return __version__
