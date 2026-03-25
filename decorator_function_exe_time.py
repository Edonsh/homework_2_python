import time

def execution_time_decorator(func):
    def wrapper():
        start_time = time.time()

        result = func()
        
        end_time = time.time()
        print(f"Execution time is : {end_time - start_time:.8f} seconds")
        return result
    
    return wrapper

@execution_time_decorator
def my_function():
    return "Finished"

print(my_function())






