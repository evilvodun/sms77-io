#!/bin/bash

FILE="requirements.txt"

if [[ -f "$FILE" ]]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
else
    echo "$FILE does not exists, trying to generate it..."
    pip install pipreqs
    pipreqs .
    pip install -r requirements.txt
fi