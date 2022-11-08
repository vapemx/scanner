import subprocess
import psutil


#Listar todos los procesos
def all_process():
    process = "powershell -Executionpolicy ByPass -Command Get-Process"
    runningProcesses = subprocess.check_output(process)
    print(runningProcesses.decode())


#Buscar los procesos con ese nombre
def one_process(name):
    try:
        process = "powershell -Executionpolicy ByPass -Command Get-Process -Name "+name
        runningProcesses = subprocess.check_output(process)
        print(runningProcesses.decode())
    except:
        return False


#Iniciar el proceso con ese nombre
def start_process(name):
    try:
        process = "powershell -Executionpolicy ByPass -Command Start-Process "+name
        runningProcesses = subprocess.check_output(process)
        print(runningProcesses.decode())
    except:
        return False


#Detener el proceso con ese nombre
def stop_process(name):
    try:
        for proc in psutil.process_iter():
            if any(procstr in proc.name() for procstr in\
                [name]):
                print(f'Killing {proc.name()}')
                proc.kill()
    except:
        return False

