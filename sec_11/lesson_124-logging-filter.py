"""
logging filter
"""
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

class NoPasswordFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message

logger.addFilter(NoPasswordFilter())

logger.info('test info')
logger.info('password=aaaaa')