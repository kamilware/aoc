#!/bin/bash

input_file="2016/inputs/d2.txt"
declare -A keypad1
keypad1["0,0"]="1" keypad1["1,0"]="2" keypad1["2,0"]="3"
keypad1["0,1"]="4" keypad1["1,1"]="5" keypad1["2,1"]="6"
keypad1["0,2"]="7" keypad1["1,2"]="8" keypad1["2,2"]="9"

x1=1
y1=1
code1=""
declare -A keypad2
keypad2["2,0"]="1"
keypad2["1,1"]="2" keypad2["2,1"]="3" keypad2["3,1"]="4"
keypad2["0,2"]="5" keypad2["1,2"]="6" keypad2["2,2"]="7" keypad2["3,2"]="8" keypad2["4,2"]="9"
keypad2["1,3"]="A" keypad2["2,3"]="B" keypad2["3,3"]="C"
keypad2["2,4"]="D"

x2=0
y2=2
code2=""

while IFS= read -r line || [[ -n "$line" ]]; do
    for (( i=0; i<${#line}; i++ )); do
        move=${line:$i:1}

        newx1=$x1
        newy1=$y1
        case $move in
            U) ((newy1--)) ;;
            D) ((newy1++)) ;;
            L) ((newx1--)) ;;
            R) ((newx1++)) ;;
        esac
        if [[ ${keypad1["$newx1,$newy1"]+_} ]]; then
            x1=$newx1
            y1=$newy1
        fi

        newx2=$x2
        newy2=$y2
        case $move in
            U) ((newy2--)) ;;
            D) ((newy2++)) ;;
            L) ((newx2--)) ;;
            R) ((newx2++)) ;;
        esac
        if [[ ${keypad2["$newx2,$newy2"]+_} ]]; then
            x2=$newx2
            y2=$newy2
        fi
    done

    code1+=${keypad1["$x1,$y1"]}
    code2+=${keypad2["$x2,$y2"]}
done < "$input_file"

echo "P1: $code1"
echo "P2: $code2"
