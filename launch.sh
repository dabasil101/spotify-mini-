#!/bin/bash
# Get the directory where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Run the script using the virtual environment's python
$DIR/.venv/bin/python3 $DIR/final_bar.py
