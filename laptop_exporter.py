from prometheus_client import start_http_server, Gauge
import psutil
import time

cpu_usage = Gauge('laptop_cpu_usage_percent', 'CPU Usage Percentage')
memory_usage = Gauge('laptop_memory_usage_percent', 'Memory Usage Percentage')
disk_usage = Gauge('laptop_disk_usage_percent', 'Disk Usage Percentage')

def collect_metrics():
    cpu_usage.set(psutil.cpu_percent())
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage('/').percent)

if __name__ == "__main__":
    start_http_server(8000)  # Expose metrics on http://localhost:8000/metrics
    while True:
        collect_metrics()
        time.sleep(5)
