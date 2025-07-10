#!/bin/bash

instructions=$(cat "2016/inputs/d1.txt")

x=0
y=0
dir=0

declare -A visited
visited["0,0"]=1
found_twice=""

IFS=',' read -ra steps <<< "$instructions"

for step in "${steps[@]}"; do
    step=$(echo "$step" | tr -d ' ')
    turn=${step:0:1}
    distance=${step:1}

    if [[ $turn == "R" ]]; then
        dir=$(( (dir + 1) % 4 ))
    else
        dir=$(( (dir + 3) % 4 ))
    fi

    for ((i=0; i<distance; i++)); do
        case $dir in
            0) ((y += 1)) ;;  # N
            1) ((x += 1)) ;;  # E
            2) ((y -= 1)) ;;  # S
            3) ((x -= 1)) ;;  # W
        esac

        key="$x,$y"
        if [[ ${visited[$key]} ]]; then
            if [[ -z "$found_twice" ]]; then
                found_twice="$key"
            fi
        else
            visited["$key"]=1
        fi
    done
done

final_distance=$(( ${x#-} + ${y#-} ))
echo "P1: $final_distance"

if [[ -n "$found_twice" ]]; then
    IFS=',' read -r fx fy <<< "$found_twice"
    dist=$(( ${fx#-} + ${fy#-} ))
    echo "P2: $dist"
else
    echo "P2: No location visited twice"
fi
