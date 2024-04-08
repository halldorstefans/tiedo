#!/bin/bash

# Telematics Service Installation Script

echo "### Telematics Service Installation ###"

# Check if Python 3.x is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3.x is required but not found."
    exit 1
fi

# Check if SQLite is installed
if ! command -v sqlite3 &> /dev/null; then
    echo "Error: SQLite is required but not found."
    exit 1
fi

CONFIG_FILE=config.yaml

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: A config file, $CONFIG_FILE, is required but not found."
fi

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

DATABASE=`sed -n 's/^data_storage: \(.*\)/\1/p' < $CONFIG_FILE`
SCHEMA=`sed -n 's/^data_schema: \(.*\)/\1/p' < $CONFIG_FILE`

echo "Creating SQLite database..."
sqlite3 $DATABASE < $SCHEMA

echo "Installation completed!"
echo "Please configure the service by editing $CONFIG_FILE."
echo "To start the service, run: python3 app.py"
