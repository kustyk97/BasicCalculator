
def is_int(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False

def try_get_float_value() -> float:
    value = input()
    if is_float(value) is True:
        value = float(value)
        return value
    else:
        print("This is not float value, try again")
        return None
    