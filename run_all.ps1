Write-Host "[*] Checking Python dependencies..."

pip install -r requirements.txt

Write-Host "`n[*] Running Process Monitor..."
python src/process_monitor.py

Write-Host "`n[*] Running Port Scanner..."
python src/port_scanner.py

Write-Host "`n[*] Running Auth Log Analyzer..."
python src/auth_log_analyzer.py

Write-Host "`n[+] All modules executed successfully."
