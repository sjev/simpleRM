#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script to build documentation using simpleRM

@author: Jev Kuznetsov
"""

from core import DataProvider
from bottle import template
from pprint import pprint

ROOT = '../requirements/simpleSE.yml'

requirements_md = '../docs/docs/requirements.md'

dp = DataProvider(ROOT)


pprint(dp.requirements)

# build requirements
txt = template("templates/requirements.tpl",dp= dp)

with open(requirements_md,'w') as fid:
    fid.write(txt)





print('done')