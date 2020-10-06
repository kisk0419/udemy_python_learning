"""
logging config
"""
import logging.config

logging.config.fileConfig('logging.ini')
#logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleExample')

logger.critical('critical')
logger.error('error')
logger.warning('warning')
logger.info('info')
logger.debug('debug')

config_dict = {
    'version': 1,
    'formatters': {
        'sampleFormatter': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'sampleHandlers': {
            'class': 'logging.StreamHandler',
            'formatter': 'sampleFormatter',
            'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['sampleHandlers'],
        'level': logging.WARNING
    },
    'loggers': {
        'configSimpleExample': {
            'handlers': ['sampleHandlers'],
            'level': logging.DEBUG,
            'propagate': 0
        }
    }
}
logging.config.dictConfig(config_dict)
logger = logging.getLogger('configSimpleExample')
logger.critical('critical')
logger.error('error')
logger.warning('warning')
logger.info('info')
logger.debug('debug')