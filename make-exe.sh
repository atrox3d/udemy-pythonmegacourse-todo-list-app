#!/bin/bash

. venv/Scripts/activate
pyinstaller --onefile --windowed --clean gui.py
