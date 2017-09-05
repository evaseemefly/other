#!_*_coding:utf-8_*_

import logging
import conf.settings

def logger(log_type):
    #创建日志模块
    logger=logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    logging.basicConfig()

    console=logging.StreamHandler()
    console.setLevel(settings.LOG_LEVEL)
    format=logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

    log_file="%s/log/%s"%(settings.BASE_DIR,settings.LOG_TYPES[log_type])
    fh=logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    formatter=logging.Formatter('%(asctime)s %(filename)s- %(levelname)s- %(message)s')

    console.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(fh)

    return logger