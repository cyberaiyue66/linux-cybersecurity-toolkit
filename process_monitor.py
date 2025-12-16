import psutil
from report import write_report

def monitor_processes(cpu_threshold=50.0, memory_threshold=100.0):
    """
    Monitors running processes and detects suspicious resource usage.

    Args:
        cpu_threshold (float): CPU usage percentage above which a process is flagged.
        memory_threshold (float): Memory usage in MB above which a process is flagged.
    """
    output_text = ""  # переменная для отчета

    print("[+] Scanning running processes...\n")

    for proc in psutil.process_iter(attrs=["pid", "name", "cpu_percent", "memory_info"]):
        try:
            pid = proc.info["pid"]
            name = proc.info["name"]
            cpu = proc.info["cpu_percent"]
            memory_mb = proc.info["memory_info"].rss / (1024 * 1024)

            # Detect high resource usage
            if cpu > cpu_threshold or memory_mb > memory_threshold:
                line = (f"[!] Suspicious process detected\n"
                        f"PID: {pid}\n"
                        f"Name: {name}\n"
                        f"CPU Usage: {cpu}%\n"
                        f"Memory Usage: {memory_mb:.2f} MB\n")
                print(line)
                output_text += line + "\n"

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Write report once all processes checked
    write_report("PROCESS MONITOR", output_text)

if __name__ == "__main__":
    monitor_processes()
