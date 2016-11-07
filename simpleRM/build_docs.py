#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script to build documentation using simpleRM

@author: Jev Kuznetsov
"""

from core import DataProvider
from bottle import template

ROOT = '../requirements/simpleSE.yml'

requirements_md = '../docs/docs/requirements.md'

dp = DataProvider(ROOT)

# build requirements
txt = template("templates/requirements.tpl",dp= dp)

with open(requirements_md,'w') as fid:
    fid.write(txt)





print('done')