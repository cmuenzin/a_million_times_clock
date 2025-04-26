# ein Beispiel mit mpremote oder ampy
import os, subprocess
files = ["core/clock_controller.py", "hal/hw_stepper.py"]
for f in files:
    subprocess.run(["mpremote", "cp", f, ":"], check=True)
subprocess.run(["mpremote", "run", "main.py"], check=True)
