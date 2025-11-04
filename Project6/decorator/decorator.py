import time

def log_time(func):
    def wrapper(*args, **kwargs):
        results = []
        for arg in args:
            start = time.perf_counter()
            result = func(arg, **kwargs)
            end = time.perf_counter()
            arg_time = end - start
            print(f"Аргумент: {arg} -> Час виконання: {arg_time:.6f} секунд")
            results.append(result)
        return results
    return wrapper