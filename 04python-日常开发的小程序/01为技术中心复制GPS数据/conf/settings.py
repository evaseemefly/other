#!_*_coding:utf-8_*_
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


LOG_LEVEL=logging.INFO

LOG_TYPES={
    'existDirLog':'currentdirlist.log',
    'copyDirLog':'copyInfo.log',
    }