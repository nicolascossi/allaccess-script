import subprocess

# Definir el número deseado de sesiones independientes de Google Chrome
num_sessions = 30

# Iniciar las sesiones independientes de Google Chrome
for i in range(num_sessions):
    subprocess.Popen(['C:\Program Files\Google\Chrome\Application\chrome.exe', '-incognito', 'https://dfentertainment.queue-it.net/?c=dfentertainment&e=taylorswift&cid=es-CL'])
