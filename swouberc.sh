#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

# Path to swouber.py in the same directory
SCRIPT="$SCRIPT_DIR/swouber.py"

# Python executable
PYTHON=python3

# Check if swouber.py exists
if [[ ! -f "$SCRIPT" ]]; then
    echo "Error: $SCRIPT not found!"
    exit 1
fi

# Run swouber.py with any passed arguments
$PYTHON "$SCRIPT" "$@"
