import inspect
from memory_profiler import memory_usage
from line_profiler import LineProfiler
import time
import os
import psutil

def profile(line_profiler_enabled=True, memory_profiler_enabled=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Start the line profiler
            if line_profiler_enabled:
                lp = LineProfiler()
                lp_wrapper = lp(func)
            else:
                lp_wrapper = func

            # Start memory tracking
            if memory_profiler_enabled:
                mem_usage_start = memory_usage(psutil.Process(os.getpid()).pid, interval=0.1, timeout=1)
            else:
                mem_usage_start = None

            # Run the function with line profiling
            start_time = time.time()
            result = lp_wrapper(*args, **kwargs)
            end_time = time.time()

            # End memory tracking
            if memory_profiler_enabled:
                mem_usage_end = memory_usage(psutil.Process(os.getpid()).pid, interval=0.1, timeout=1)
            else:
                mem_usage_end = None

            # Write the line profiler results to a file
            with open('profile_log.txt', 'w') as f:
                if line_profiler_enabled:
                    lp.print_stats(stream=f)

                # Calculate and write memory usage to the file
                if memory_profiler_enabled:
                    memory_used = max(mem_usage_end) - min(mem_usage_start)
                    f.write(f"\nMemory used: {memory_used} MiB\n")

                # Write time taken to the file
                f.write(f"Time taken: {end_time - start_time} seconds\n")

            return result
        return wrapper
    return decorator
