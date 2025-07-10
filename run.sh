#!/bin/bash

YEAR=$1
DAY=$2

if [ -z "$YEAR" ] || [ -z "$DAY" ]; then
    echo "Usage: $0 <year> <day>"
    exit 1
fi

case $YEAR in
    2015)
        FILE="2015/d${DAY}.py"
        if [ -f "$FILE" ]; then
            python3 "$FILE"
        else
            echo "File not found: $FILE"
            exit 1
        fi
        ;;

    2016)
        FILE="2016/d${DAY}.sh"
        if [ -f "$FILE" ]; then
            bash "$FILE"
        else
            echo "File not found: $FILE"
            exit 1
        fi
        ;;

    *)
        echo "Year $YEAR not supported."
        exit 1
        ;;
esac
