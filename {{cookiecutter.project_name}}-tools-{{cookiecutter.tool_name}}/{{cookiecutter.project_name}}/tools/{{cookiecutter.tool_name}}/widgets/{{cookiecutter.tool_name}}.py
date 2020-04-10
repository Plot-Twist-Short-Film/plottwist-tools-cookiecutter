#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{{cookiecutter.tool_description}}
"""

from __future__ import print_function, division, absolute_import

__author__ = "{{cookiecutter.author}}"
__license__ = "MIT"
__maintainer__ = "{{cookiecutter.maintainer}}"
__email__ = "{{cookiecutter.email}}"

from Qt.QtWidgets import *

import tpDcc as tp

import artellapipe


class {{cookiecutter.tool_class}}ToolWidget(artellapipe.ToolWidget, object):

    def __init__(self, project, config, settings, parent):
        super({{cookiecutter.tool_class}}ToolWidget, self).__init__(project=project, config=config, settings=settings, parent=parent)

    def ui(self):
        super({{cookiecutter.tool_class}}ToolWidget, self).ui()
