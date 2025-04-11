import psutil
import time
import socket


def monitor_network():
    # Get initial network stats
    net_io_counters_start = psutil.net_io_counters()

    time.sleep(1)  # Wait 1 second

    # Get updated network stats
    net_io_counters_end = psutil.net_io_counters()

    # Calculate bytes sent/received per second
    bytes_sent = net_io_counters_end.bytes_sent - net_io_counters_start.bytes_sent
    bytes_recv = net_io_counters_end.bytes_recv - net_io_counters_start.bytes_recv

    print(f"Network usage: {bytes_sent / 1024:.2f} KB/s sent, {bytes_recv / 1024:.2f} KB/s received")

    # List all network connections
    connections = psutil.net_connections()
    print(f"Active network connections: {len(connections)}")

    # List network interfaces
    interfaces = psutil.net_if_addrs()
    print("\nNetwork interfaces:")
    for interface, addresses in interfaces.items():
        print(f"  {interface}:")
        for address in addresses:
            if address.family == socket.AF_INET:  # IPv4
                print(f"    IPv4: {address.address}")
            elif address.family == socket.AF_INET6:  # IPv6
                print(f"    IPv6: {address.address}")


monitor_network()