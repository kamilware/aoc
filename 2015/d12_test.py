from d12 import p1, p2

p1_inputs = [
    ("[1,2,3]", 6),
    ('{"a":2,"b":4}', 6),
    ("[[[3]]]", 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}]', 0),
    ("{}", 0),
    ("[]", 0),
]

p2_inputs = [
    ("[1,2,3]", 6),
    ('[1,{"c":"red","b":2},3]', 4),
    ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
    ('[1,"red",5]', 6),
]

if __name__ == "__main__":
    for input, exp in p1_inputs:
        res = p1(input)
        try:
            assert exp == res
        except AssertionError:
            print(f"1 | input: {input}, expected: {exp}, actual: {res}")

    for input, exp in p2_inputs:
        res = p2(input)
        try:
            assert exp == res
        except AssertionError:
            print(f"1 | input: {input}, expected: {exp}, actual: {res}")
