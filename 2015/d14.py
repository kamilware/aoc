import re
from typing import Dict, List, Tuple

PATTERN = r"^(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<time>\d+) seconds?, but then must rest for (?P<rest>\d+) seconds?"


def parse_line(line: str):
    m = re.match(PATTERN, line)
    d: Dict[str, Tuple[int, int, int]] = {}
    # name: speed, time, rest

    if m:
        data = m.groupdict()
        d[data["name"]] = int(data["speed"]), int(data["time"]), int(data["rest"])

    return d


def p1(lines: List[str], total_time: int) -> int:
    reindeers: Dict[str, Tuple[int, int, int]] = {}
    for line in lines:
        reindeers.update(parse_line(line))

    max_distance = 0

    for _, (speed, fly_time, rest_time) in reindeers.items():
        cycle_time = fly_time + rest_time
        full_cycles = total_time // cycle_time
        remaining_time = total_time % cycle_time
        extra_fly = min(remaining_time, fly_time)
        distance = (full_cycles * fly_time + extra_fly) * speed
        max_distance = max(max_distance, distance)

    return max_distance


def p2(lines: List[str], total_time: int = 2503) -> int:
    reindeers: Dict[str, Tuple[int, int, int]] = {}
    for line in lines:
        reindeers.update(parse_line(line))

    distances = {name: 0 for name in reindeers}
    states = {name: "flying" for name in reindeers}
    fly_times = {name: reindeers[name][1] for name in reindeers}
    scores = {name: 0 for name in reindeers}
    remaining_times = {name: fly_times[name] for name in reindeers}

    for _ in range(1, total_time + 1):
        for name, (speed, fly_time, rest_time) in reindeers.items():
            if states[name] == "flying":
                distances[name] += speed
                remaining_times[name] -= 1
                if remaining_times[name] == 0:
                    states[name] = "resting"
                    remaining_times[name] = rest_time
            else:
                remaining_times[name] -= 1
                if remaining_times[name] == 0:
                    states[name] = "flying"
                    remaining_times[name] = fly_time

        max_distance = max(distances.values())
        for name in reindeers:
            if distances[name] == max_distance:
                scores[name] += 1

    return max(scores.values())


if __name__ == "__main__":
    with open("2015/inputs/d14.txt") as f:
        lines = f.read().splitlines()

    print(f"P1: {p1(lines, 2503)}")
    print(f"P2: {p2(lines)}")
