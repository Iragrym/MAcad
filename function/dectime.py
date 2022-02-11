
import time

def time_in_file(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        with open('function_time.txt', 'w') as f:
        f.write(f"Duration of {func.__name__} is {end-start} seconds")
        f.close()
        return result 
    return wrapper



@time_in_file
def range_sum(end: int) -> int:
    step = 1  if end > 0 else -1
    start = 0

    sm = 0
    while start != end:
        start += step
        sm += start
    return sm

range_sum(10_000)