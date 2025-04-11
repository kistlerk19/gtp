import time
import psutil

# print(psutil.cpu_count())
# print(psutil.cpu_percent())
# print(psutil.virtual_memory().percent)

def display_usage(cpu_usage, memory_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bars = '▋' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    memory_percent = (memory_usage / 100.0)
    mem_bars = '▊' * int(memory_percent * bars) + '-' * (bars - int(memory_percent * bars))

    print(f"\rCPU usage: |{cpu_bars}| {cpu_usage:.2f}%   ", end="")
    print(f"Memory usage: |{mem_bars}| {memory_usage:.2f}%   ", end="\r")

while True:
    # print("System Monitor Starting... Press Ctrl+C to stop.\n")
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 50)
    time.sleep(1)