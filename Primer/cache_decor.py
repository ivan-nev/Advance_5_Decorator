
def cached_decor(cache_size):

    def _cached_decor(old_function):
        CACHE = {}

        def new_function(*args, **kwargs):
            key = f'{args}{kwargs}'
            if key in CACHE:
                return CACHE[key]
            result = old_function(*args, **kwargs)
            if len(CACHE) > cache_size:
                CACHE.popitem()
            CACHE[key] = result
            return result

        return new_function

    return _cached_decor
