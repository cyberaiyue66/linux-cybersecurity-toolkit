import os

def check_startup_programs():
    """
    Checks startup programs on a Linux system.
    """

    startup_path = "/etc/rc.local"

    if os.path.exists(startup_path):
        print("[+] Startup configuration file found.")
    else:
        print("[!] Startup configuration file not found.")

if __name__ == "__main__":
    check_startup_programs()
