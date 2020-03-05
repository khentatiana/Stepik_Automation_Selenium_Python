import self as self

try:
    assert abs(-42) == 42, "Should be 42"
    assert abs(-40) == 40, "Should be 40"
    assert abs(-45) == 41, "Should be 45"
    assert abs(-2) == 2, "Should be 2"

finally:
    print("End of testing")

