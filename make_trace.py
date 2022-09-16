import datetime
from typing import Callable, Any

def make_trace(path: str) -> Callable:

    def trace(old_function: Callable) -> Callable:

        def new_function(*args, **kwargs) -> Any:
            result = old_function(*args, **kwargs)

            with open(path, 'a') as log:
                log.write(f'{datetime.datetime.utcnow()}: called {old_function.__name__}\n'
                          f'\t args: {args}\n'
                          f'\t kwargs: {kwargs}\n'
                          f'\t result: {result}\n\n')

            return result
        return new_function
    return trace