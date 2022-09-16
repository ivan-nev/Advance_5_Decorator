import datetime
import logging
from logging.handlers import RotatingFileHandler
from typing import Callable, Any

def make_log(path: str) -> Callable:

    def log(old_function: Callable) -> Callable:
        logger = logging.getLogger(path)
        logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(path, backupCount=10, maxBytes=1000000)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        def new_function(*args, **kwargs) -> Any:
            result = old_function(*args, **kwargs)

            logger.info(f'called: {old_function.__name__}\n'
                        f'\t args: {args}\n'
                        f'\t kwargs: {kwargs}\n'
                        f'\t result: {result}')
            return result

        return new_function

    return log