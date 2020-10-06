"""
logger
"""
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info('test info')

logger.setLevel(logging.DEBUG)

logger.debug('test debug')