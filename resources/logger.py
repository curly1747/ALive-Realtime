import logging.config
import logging
from logging import Filter, StreamHandler
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
import os

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)

class LoggingLevelFilter(logging.Filter):
    def __init__(self, allow_level):
        super().__init__()
        self.allow_level = allow_level

    def filter(self, rec):
        return rec.levelno in self.allow_level


class LoggerConfig:
    log_colors = {
        "DEBUG": "purple",
        "INFO": "green",
        "WARNING": "white",
        "ERROR": "bold_red",
        "CRITICAL": "black,bg_red",
    }

    datetime_format = '%Y-%m-%d %H:%M:%S'
    info_format = '%(asctime)s [%(levelname)8s] %(message)s'
    handlers = ['console', 'file']

    info_filters = [INFO, DEBUG, WARNING, ERROR, CRITICAL]

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': info_format,
                'datefmt': datetime_format,
            },
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': '%(log_color)s' + info_format,
                'datefmt': datetime_format,
                'log_colors': log_colors,
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
                'stream': 'ext://sys.stdout',
                'filters': ['infofilter', ]
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': f'{os.getcwd()}/log/log.log',
                'filters': ['infofilter', ],
            },
        },
        'filters': {
            'infofilter': {
                '()': LoggingLevelFilter,
                'allow_level': info_filters,
            },
        },
        'loggers': {
            'ALive': {
                'handlers': handlers,
                'level': DEBUG,
                'propagate': True,
            },
        },
    }


# Init app logging
logging.config.dictConfig(LoggerConfig.LOGGING)
