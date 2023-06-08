import inspect
from memory_profiler import memory_usage
from line_profiler import LineProfiler
import time
import os
import psutil

def profile(func):
    def wrapper(*args, **kwargs):
        # Get the source code of the function
        source_code = inspect.getsource(func)

        # Start the line profiler
        lp = LineProfiler()
        lp.add_function(func)
        lp.runctx(source_code, globals(), locals())

        # Start memory tracking
        mem_usage_start = memory_usage(psutil.Process(os.getpid()).pid, interval=0.1, timeout=1)

        # Run the function
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        # End memory tracking
        mem_usage_end = memory_usage(psutil.Process(os.getpid()).pid, interval=0.1, timeout=1)

        # Write the line profiler results to a file
        with open('profile_log.txt', 'w') as f:
            lp.print_stats(stream=f)

            # Calculate and write memory usage to the file
            memory_used = max(mem_usage_end) - min(mem_usage_start)
            f.write(f"\nMemory used: {memory_used} MiB\n")

            # Write time taken to the file
            f.write(f"Time taken: {end_time - start_time} seconds\n")

        return result

    return wrapper
