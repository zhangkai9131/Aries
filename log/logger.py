#!/usr/bin/env python
#-*- coding: utf-8 -*-
####################################
#    logger.py
#    日志功能封装
#
#    2018.1.26     shanghai
####################################
import os
import sys
import threading
import logging
from logging.handlers import RotatingFileHandler

def ERROR(*args):
    if hasattr(threading.currentThread(), '_logger'):
        threading.currentThread()._logger.error(*args)

def WARNING(*args):
    if hasattr(threading.currentThread(), '_logger'):
        threading.currentThread()._logger.warning(*args)

def INFO(*args):
    if hasattr(threading.currentThread(), '_logger'):
        threading.currentThread()._logger.info(*args)

def DEBUG(*args):
    if hasattr(threading.currentThread(), '_logger'):
        threading.currentThread()._logger.debug(*args)

def GetLogger(strLogPath, strLogName, nLevel, logThread=None):
    strLogFile = '%s.log' % os.path.join(strLogPath, strLogName)
    formatter = logging.Formatter(
                    '%(asctime)s %(levelname)-7s:%(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S')
    RtHandler = RotatingFileHandler(
                    strLogFile, 
                    maxBytes = 2 * 1024 * 1024, 
                    backupCount = 10)
    RtHandler.setLevel(nLevel)
    RtHandler.setFormatter(formatter)

    Console = logging.StreamHandler(sys.stdout)
    Console.setLevel(nLevel)
    Console.setFormatter(formatter)

    if logThread is None:
        logThread = threading.currentThread()
    logThread._logger = logging.getLogger(strLogName)
    logThread._logger.addHandler(RtHandler)
    logThread._logger.addHandler(Console)
    logThread._logger.setLevel(nLevel)

    RtHandler.doRollover()

#####################################
# for test
#####################################
if __name__ == '__main__':
    try:
        GetLogger('/home/ap/nas/logs', 'testlogger', logging.DEBUG)
        DEBUG('------------DEBUG------------')
        INFO('------------INFO------------')
        WARNING('------------WARNING------------')
        ERROR('------------ERROR------------')
    except:
        traceback.print_exc()
#####################################
# test end
#####################################
