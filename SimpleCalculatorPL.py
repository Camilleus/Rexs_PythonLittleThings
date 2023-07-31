result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if wait_for_number:
            input_value = input("Podaj liczbę: ")
            operand = float(input_value)
            wait_for_number = False
        else:
            input_value = input("Podaj operator (+, -, *, /): ")
            if input_value not in ['+', '-', '*', '/']:
                raise ValueError(
                    f"{input_value} nie jest '+' lub '-' lub '/' lub '*'")
            if operator == input_value:
                raise ValueError(
                    "Błąd! Wprowadzono operator dwa razy z rzędu!")
            operator = input_value
            wait_for_number = True

        if operand is not None and operator is not None:
            if operator == '+':
                result = result + operand if result is not None else operand
            elif operator == '-':
                result = result - operand if result is not None else -operand
            elif operator == '*':
                result = result * operand if result is not None else 0
            elif operator == '/':
                if operand == 0:
                    raise ZeroDivisionError("Nie można dzielić przez zero!")
                result = result / operand if result is not None else 0

            operand = None
            operator = None

    except ValueError as ve:
        print(f"Błąd: {ve}")
    except ZeroDivisionError as zde:
        print(f"Błąd: {zde}")

    if input_value == '=':
        if result is not None:
            print(f"Wynik: {result}")
        else:
            print("Nie podano żadnych operacji.")
        break
