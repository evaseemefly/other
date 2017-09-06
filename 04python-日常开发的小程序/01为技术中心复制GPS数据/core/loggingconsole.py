
# import conf.settings as st
import core.loghelper as lg
import logging


def do():

    log=lg.logger('myLog')
    log.info('测试测试')

    # fmt = '%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s: %(message)s'
    # logging.basicConfig(level=logging.DEBUG,
    #                     format=fmt,
    #                     filename='d:/logs.txt',
    #                     filemode='w',
    #                     datefmt='%a, %d %b %Y %H:%M:%S'
    #                     )
    #
    # console = logging.StreamHandler()
    # console.setLevel(logging.INFO)
    #
    # formatter = logging.Formatter(fmt)
    # console.setFormatter(formatter)
    # logging.getLogger().addHandler(console)
    #
    # logging.debug('this is a debug level message')
