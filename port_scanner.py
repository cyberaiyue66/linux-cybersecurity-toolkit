import subprocess
from report import write_report

def scan_ports():
    """
    Scans open network ports on Windows using netstat.
    -a : all connections
    -n : numeric addresses
    -o : show PID
    """
    result = subprocess.run(
        ["netstat", "-ano"],
        capture_output=True,
        text=True
    )

    print("[+] Open network ports detected:")
    print(result.stdout)

    write_report(
        "PORT SCANNER",
        result.stdout
    )

if __name__ == "__main__":
    scan_ports()
