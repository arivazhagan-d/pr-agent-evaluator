from typing import Optional


def expression_evaluator(expression: str) -> Optional[float]:
    """
        Take mathematical expression and gives the answer by evaluating it.
    Args:
        input_expression (str): mathematical expression with
        numbers and arithmetic operators.
    Returns:
        float: answer to mathematical expression.
    """
    accepted_characters = [
        "+",
        "-",
        "*",
        "/",
        "//",
        "%",
        " ",
        "(",
        ")",
        ".",
    ]

    # Checking the expression contains only numbers and accepted characters.
    for character in expression:
        if character.isnumeric() or character in accepted_characters:
            continue
        print("Enter a valid mathematical expression.")
        return None

    # Parsing and compiling the input expression to check whether
    # it's a valid mathematical expression.
    try:
        compiled_expression = compile(input_expression, "<string>", "eval")
    except SyntaxError:
        print("Enter correct expression to evaluate")
        return None

    # Checking whether the input expression consists of only
    # numbers and mathematical operators or else raising a NameError.
    try:
        if compiled_expression.co_names:
            raise NameError(
                "Use of numbers and mathematical operators are only allowed."
            )
    except NameError as error:
        print(error)
        return None

    # Evaluating the mathematical expression with prevention of security risks
    # by not allowing global namespaces.
    answer = float(eval(compiled_expression, {"__builtins__": {}}, {}))
    answer = round(answer, 2)

    return answer


def DoStuff():
    print("This is doing something.")


def helper():
    print("This is helper.")


def unused_function():
    pass


if __name__ == "__main__":
    while True:
        input_expression = input("Enter a mathematical expression to evaluate: ")
        result = expression_evaluator(input_expression)
        if result is not None:
            print(result)
            break
