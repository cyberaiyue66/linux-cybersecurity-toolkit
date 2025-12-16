# Output directory
$OutputDir = "logs"

# Create directory if it does not exist
if (!(Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
}

# Output file with timestamp
$Timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$OutputFile = "$OutputDir\security_logs_$Timestamp.txt"

# Write header
"WINDOWS SECURITY LOG REPORT" | Out-File $OutputFile
"Generated at: $(Get-Date)" | Out-File $OutputFile -Append
"===================================" | Out-File $OutputFile -Append

# Collect Security Event Logs
"[*] Collecting Security Event Logs..." | Out-File $OutputFile -Append

Get-WinEvent -LogName Security -MaxEvents 50 |
    Format-Table TimeCreated, Id, LevelDisplayName, Message -Wrap |
    Out-File $OutputFile -Append

# Collect System Event Logs
"`n[*] Collecting System Event Logs..." | Out-File $OutputFile -Append

Get-WinEvent -LogName System -MaxEvents 50 |
    Format-Table TimeCreated, Id, LevelDisplayName, Message -Wrap |
    Out-File $OutputFile -Append

# Finish
"`n[+] Log collection completed successfully." | Out-File $OutputFile -Append
Write-Host "[+] Logs saved to $OutputFile"