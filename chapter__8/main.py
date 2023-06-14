
# just for giveing message
import logging

logging.basicConfig(filename='loging.text', format='%(asctime)s%(name)s%(levelname)s', filemode='r')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Soumik Sarkar")
logger.info("'just an information'")
logger.warning("It's a Warning")
logger.error('did you try to do this')
