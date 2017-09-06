#!_*_coding:utf-8_*_
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCE_DIR=r"E:\03协同开发\other\04python-日常开发的小程序\SOURCE"
TARGET_DIR=r"E:\03协同开发\other\04python-日常开发的小程序\TARGET"

STATIONS=['测试海洋站',]


LOG_LEVEL=logging.INFO

LOG_TYPES={
    'existDirLog':'currentdirlist.log',
    'copyDirLog':'copyInfo.log',
    'myLog':'console.log'
    }