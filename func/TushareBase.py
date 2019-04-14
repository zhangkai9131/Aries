# -*- coding: utf-8 -*-
# Filename:TuShareBase.py

import tushare as ts

class TuShareBase(object):
    def __init__(self):
        try:
            self.pro = ts.pro_api()
        except Exception as e:
            raise IOError('invalid value: %s' % e)

