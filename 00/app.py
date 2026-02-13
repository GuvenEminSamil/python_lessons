from settings import settings
from logs import logger

if __name__ == '__main__':
    logger.info(settings.secret_key)