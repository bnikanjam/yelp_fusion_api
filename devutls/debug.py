import colorama
from functools import wraps
from timeit import default_timer as timer


def print_blue(text):
    print(f"{colorama.Fore.BLUE}{text}{colorama.Fore.RESET}")


def print_red(text):
    print(f"{colorama.Fore.RED}{text}{colorama.Fore.RESET}")


def print_yellow(text):
    print(f"{colorama.Fore.YELLOW}{text}{colorama.Fore.RESET}")


def print_green(text):
    print(f"{colorama.Fore.GREEN}{text}{colorama.Fore.RESET}")


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return_of_decorated_func = func(*args, **kwargs)
        print_yellow(f'{func.__name__}({args}, {kwargs}) -> {return_of_decorated_func}')
        return return_of_decorated_func
    return wrapper


def benchmark(func):
    """Print runtime of the decorated function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timer()
        return_of_decorated_func = func(*args, **kwargs)
        run_time = timer() - start_time

        if run_time >= 1:
            print(f"\nRUNTIME of {func.__name__}: {round(run_time, 2)} seconds.")
        elif run_time >= 10 ** -3:
            print(f"\nRUNTIME of {func.__name__}: {round(run_time*10**3, 2)} milliseconds.")
        elif run_time >= 10 ** -6:
            print(f"\nRUNTIME of {func.__name__}: {round(run_time*10**6, 2)} microseconds.")
        elif run_time >= 10 ** -9:
            print(f"\nRUNTIME of {func.__name__}: {round(run_time*10**9, 2)} nanoseconds.")

        return return_of_decorated_func

    return wrapper
