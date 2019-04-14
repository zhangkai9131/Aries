# -*- coding: utf-8 -*-
# Filename:DataSourceConfig.py

import xml.etree.ElementTree as ET

class DataSourceConfig(object):
    def __init__(self, id, host, port, db, user, pwd):
        self.__m_id = id
        self.__m_host = host
        self.__m_port = port
        self.__m_db = db
        self.__m_user = user
        self.__m_pwd = pwd