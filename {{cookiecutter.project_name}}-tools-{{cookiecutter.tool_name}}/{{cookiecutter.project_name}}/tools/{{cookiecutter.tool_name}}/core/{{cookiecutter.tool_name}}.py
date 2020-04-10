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

import artellapipe

# Defines ID of the tool
TOOL_ID = '{{cookiecutter.project_name}}-tools-{{cookiecutter.tool_name}}'

# We skip the reloading of this module when launching the tool
no_reload = True


class {cookiecutter.tool_class}Tool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super({cookiecutter.tool_class}Tool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': '{{cookiecutter.tool_nice_name}}',
            'id': TOOL_ID,
            'logo': '{{cookiecutter.tool_name}}_logo',
            'icon': '{{cookiecutter.tool_name}}',
            'help_url': 'https://{{cookiecutter.project_name_alt}}-short-film.github.io/{{cookiecutter.project_name}}-docs/pipeline/pipeline/tools/{{cookiecutter.tool_name}}/',
            'kitsu_login': {{cookiecutter.kitsu_login}},
            'tooltip': '{{cookiecutter.tool_description}}',
            'tags': ['{{cookiecutter.project_name}}', '{{cookiecutter.tool_tag}}'],
            'sentry_id': '{{cookiecutter.sentry_id}}',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': '{{cookiecutter.tool_nice_name}}', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': '{{cookiecutter.department}}',
                 'type': 'menu', 'children': [{'id': '{{cookiecutter.project_name}}-tools-{{cookiecutter.tool_name}}', 'type': 'tool'}]}],
            'shelf': [
                {'name': '{{cookiecutter.department}}',
                 'children': [{'id': '{{cookiecutter.project_name}}-tools-{{cookiecutter.tool_name}}', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class {{cookiecutter.tool_class}}Toolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super({{cookiecutter.tool_class}}Toolset, self).__init__(*args, **kwargs)

    def contents(self):

        from {{cookiecutter.project_name}}.tools.{{cookiecutter.tool_name}}.widgets import {{cookiecutter.tool_name}}

        tool_inst = {{cookiecutter.tool_name}}.{{cookiecutter.tool_class}}ToolWidget(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [tool_inst]
