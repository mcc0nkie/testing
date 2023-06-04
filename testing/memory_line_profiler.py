from memory_profiler import memory_usage, profile as mem_profile
from line_profiler import LineProfiler
import time
import os
import psutil

def profile(func):
    def wrapper(*args, **kwargs):
        # Initialize line profiler
        line_prof = LineProfiler()
        wrapped = line_prof(func)

        # Memory profiling
        mem_profile_start = memory_usage(psutil.Process(os.getpid()).pid, interval=0.1, timeout=1)
        
        start_time = time.time()
        # Call function
        result = wrapped(*args, **kwargs)
        end_time = time.time()

        mem_profile_end = memory_usage(psutil.Process(os.getpid()).pid, interval=0.1, timeout=1)
        
        # Write the line profiler results to a file
        with open('profiler_results.txt', 'a+') as f:  # Open in append mode
            f.write(f"Profiler results for function {func.__name__}:\n")
            line_prof.print_stats(stream=f)

            # Calculate and write memory usage to the file
            memory_used = max(mem_profile_end) - min(mem_profile_start)
            f.write(f"\nMemory used: {memory_used} MiB\n")
            f.write(f"Time taken: {end_time - start_time} seconds\n")
            f.write("\n" + "-" * 50 + "\n")  # Separator for readability
        
        return result

    return wrapper
