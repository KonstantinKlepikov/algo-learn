from time import time
from copy import deepcopy


def short_timeit(function):
    """Used for display a time of solution run
    """
    def wrapper(*args, **kwargs):
        dist = kwargs.get('dist', None)
        if not dist:
            ts = time()
            result = function(*args, **kwargs)
            te = time()
            res = (te-ts) * 1000000
            print(f'Short timeit {kwargs=}, took: {res} mks')
            return result
        else:
            del kwargs['dist']
            ts = time()
            function(*args, **kwargs)
            te = time()
            return (te-ts) * 1000000
    return wrapper


def long_timeit(dist=10000):
    """Used for measure a median time of solution run
    """
    def parametrized(function):
        def wrapper(*args, **kwargs):
            measure = 0
            kwargs['dist'] = dist
            for _ in range(dist):
                measure += function(*deepcopy(args), **deepcopy(kwargs))
            del kwargs['dist']
            print(
                f'Long timeit {kwargs=} in range {dist}'
                f'took: {measure / dist} mks'
                    )
        if dist:
            return wrapper
        else:
            return parametrized
    return parametrized


if __name__ == '__main__':

    # example
    @short_timeit
    def what(n, m=0):
        count = 0
        for _ in range(1000):
            count += n + m

    what(n=2)

    long_timeit()(what)(n=2)
