from datetime import datetime

def write_report(section, content):
    """
    Writes scan results to report.txt with timestamp
    """
    with open("report.txt", "a", encoding="utf-8") as f:
        f.write("\n" + "=" * 60 + "\n")
        f.write(f"{section}\n")
        f.write(f"Time: {datetime.now()}\n")
        f.write("-" * 60 + "\n")
        f.write(content + "\n")
