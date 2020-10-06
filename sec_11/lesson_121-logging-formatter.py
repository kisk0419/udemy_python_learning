"""
logging formatter
"""

import logging

formatter = '%(asctime)s:%(levelname)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=formatter)

logging.info('test message')