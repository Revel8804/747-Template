import subprocess, sys, os
path = getattr(sys, '_MEIPASS', os.getcwd())
ps1path = path + "\XboxVersionMSFS747Template.ps1"
psxmlgen = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             ps1path])
result = psxmlgen.wait()
