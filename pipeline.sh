#!/bin/bash

PAIRS=(
    "2015 python3"
)

for pair in "${PAIRS[@]}"; do
    set -- $pair
    YEAR=$1
    INTERPRETER=$2
    DIR="$YEAR"

    echo "== Running tests in $DIR with $INTERPRETER =="

    if [ ! -d "$DIR" ]; then
        echo "Directory not found: $DIR"
        continue
    fi

    FOUND_FILES=false
    for FILE in "$DIR"/*_test.py; do
        if [ -f "$FILE" ]; then
            FOUND_FILES=true
            echo "Running $FILE"
            $INTERPRETER "$FILE"
        fi
    done

    if [ "$FOUND_FILES" = false ]; then
        echo "No _test.py files found in $DIR"
    fi

    echo
done
