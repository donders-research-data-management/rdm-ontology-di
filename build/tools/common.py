#!/usr/bin/env python
import logging
import inspect
from colorlog import ColoredFormatter

lc_formatter = ColoredFormatter(
    "%(log_color)s[%(levelname)-8s:%(name)s] %(message)s%(reset)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red',
    }
)

loggers = {}

def getMyLogger(name=None, lvl=0):

    global loggers

    _lvl = [ logging.WARNING, logging.ERROR, logging.INFO, logging.DEBUG ]

    if name is None:
        name = inspect.stack()[1][3]

    if not loggers.get(name):

        ## create new logger object
        _logger = logging.getLogger(name)
        _logger.setLevel(_lvl[lvl])

        ## add logger handlers
        _s_hdl = logging.StreamHandler()
        _s_hdl.setFormatter(lc_formatter)

        _logger.addHandler(_s_hdl)

        loggers[name] = _logger

    return loggers.get(name)