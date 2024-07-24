from mathOperations import add, sub, mul, div

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
    
def main():

    welcome_message = """Welcome in my calculator
You can make math operations like add, substract, multiplication and divide with two values."""
    print(welcome_message)
    main_menu_options = """1.add
2.substract
3.multiplication
4.divide
5.exit"""
    while True:
        print(main_menu_options)
        input_value = input()
        if is_int(input_value) is False:
            print("unknow value")
            continue
        input_value = int(input_value)
        if input_value not in [1,2,3,4,5]:
            print("unknow value")
            continue
        if input_value == 5:
            print("Bye:D")
            break
        else:
            first_value = None
            second_value = None
            while True:
                print("Write first float value:", sep=" ")
                first_value = try_get_float_value()
                if first_value is not None:
                    break

            while True:
                print("Write second float value:", sep=" ")
                second_value = try_get_float_value()
                if second_value is not None:
                    break

            if input_value == 1:
                print("Result: " + str(add(first_value, second_value)))
            if input_value == 2:
                print("Result: " + str(sub(first_value, second_value)))
            if input_value == 3:
                print("Result: " + str(mul(first_value, second_value)))
            if input_value == 4:
                print("Result: " + str(div(first_value, second_value)))

if __name__ == "__main__":
    main()