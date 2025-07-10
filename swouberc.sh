#!/bin/bash

# Run Swouber script

# Optional: Set Python executable if needed
PYTHON=python3

# Path to your swouber.py script
SCRIPT="swouber.py"

# Check if the script exists
if [[ ! -f "$SCRIPT" ]]; then
    echo "Error: $SCRIPT not found!"
    exit 1
fi

# Run the script
$PYTHON "$SCRIPT"
