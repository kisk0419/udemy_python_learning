"""
logging handler
"""
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
handler = logging.FileHandler('lesson_123.log')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info('test info')
logger.debug('test debug')
