#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5

    result1 = calculator_1.add(a, b)
    result2 = calculator_1.sub(a, b)
    result3 = calculator_1.mul(a, b)
    result4 = calculator_1.div(a, b)

    print(f"{a} + {b} = {result1}")
    print(f"{a} - {b} = {result2}")
    print(f"{a} * {b} = {result3}")
    print(f"{a} / {b} = {result4}")
