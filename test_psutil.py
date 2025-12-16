import psutil
print(psutil.cpu_percent())

# Проверяем список процессов
for proc in psutil.process_iter(['pid', 'name']):
    print(proc.info)