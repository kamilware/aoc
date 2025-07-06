#!/bin/bash

YEAR=$1
DAY=$2

if [ "$YEAR" = "2015" ]; then
    FILE="2015/d${DAY}_test.py"
    if [ -f "$FILE" ]; then
        python3 "$FILE"
    else
        echo "File not found: $FILE"
        exit 1
    fi
else
    echo "Year $YEAR not supported."
    exit 1
fi
