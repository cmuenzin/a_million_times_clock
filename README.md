# Million-Times-Clock

Inspiriert von der Million Times Clock by HS1982

**Ziel:** Simulation und Steuerung von 24 Uhren mit je 2 Steppern  
**Technologien:** Python, Pygame, MicroPython auf ESP32

## Setup (Simulation)
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python sim/main.py`

## Deployment (ESP32)
1. Firmware: MicroPython auf ESP32 flashen
2. `python hw/flash.py`  – lädt `hal/hw_stepper.py` und `core/` auf das Gerät
3. ESP32 startet automatisch und fährt die Uhren

## Projektstruktur
…
