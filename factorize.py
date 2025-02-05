import time
from multiprocessing import Pool, cpu_count


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_sync(numbers):
    return [factorize(number) for number in numbers]

def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    result_sync, time_sync = measure_time(factorize_sync, numbers)
    print(f"Sync factorize for {numbers}: {result_sync}, Time: {time_sync:.4f} seconds")

    result_parallel, time_parallel = measure_time(factorize_parallel, numbers)
    print(f"Parallel factorize for {numbers}: {result_parallel}, Time: {time_parallel:.4f} seconds")
