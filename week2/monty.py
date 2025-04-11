import psutil
import time
from ping3 import ping
from datetime import datetime


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.total, mem.used, mem.free, mem.percent


def get_disk_io():
    io = psutil.disk_io_counters()
    return io.read_bytes, io.write_bytes


def get_network_io():
    net = psutil.net_io_counters()
    return net.bytes_sent, net.bytes_recv


def get_latency(host="8.8.8.8"):
    delay = ping(host, timeout=1)
    if delay is None:
        return -1
    return round(delay * 1000, 2)  # ms


def human_readable_bytes(num):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024:
            return f"{num:.2f} {unit}"
        num /= 1024


def monitor(interval=2):
    print("System Monitor Starting... Press Ctrl+C to stop.\n")
    try:
        while True:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu = get_cpu_usage()
            total, used, free, mem_pct = get_memory_usage()
            rbytes, wbytes = get_disk_io()
            sent, recv = get_network_io()
            latency = get_latency()

            print(f"[{now}] CPU: {cpu}% | Memory: {mem_pct}% ({human_readable_bytes(used)}/{human_readable_bytes(total)})")
            print(f"Disk Read: {human_readable_bytes(rbytes)}, Write: {human_readable_bytes(wbytes)}")
            print(f"Net Sent: {human_readable_bytes(sent)}, Recv: {human_readable_bytes(recv)}")
            print(f"Latency to 8.8.8.8: {latency if latency != -1 else 'Timeout'} ms")
            print("-" * 80)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    monitor()
