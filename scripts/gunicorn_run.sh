#!/bin/bash

CONFIG_FILE=config.yaml

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: A config file, $CONFIG_FILE, is required but not found."
fi

PORT=`sed -n 's/^port: \(.*\)/\1/p' < $CONFIG_FILE`

gunicorn -w 2 -b 0.0.0.0:$PORT --preload 'src:create_app()'