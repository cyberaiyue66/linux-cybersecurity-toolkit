from report import write_report

def analyze_logs():
    """
    Analyzes authentication log file
    and counts failed login attempts.
    """
    log_path = "data/test_auth.log"
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            failed = [line for line in f if "Failed" in line]

        print(f"[!] Failed login attempts detected: {len(failed)}")

        # Отправляем данные в общий отчёт
        write_report(
            "AUTH LOG ANALYZER",
            f"Failed login attempts: {len(failed)}"
        )

    except FileNotFoundError:
        print("[!] Log file not found:", log_path)
        write_report(
            "AUTH LOG ANALYZER",
            "[!] Log file not found: " + log_path
        )

if __name__ == "__main__":
    analyze_logs()
