from operator import add, mul, sub, truediv
from typing import List, Optional, Union

ops = {"+": add, "-": sub, "*": mul, "/": truediv}

def prefix_evaluate(prefix_evaluation: str) -> int:
    if prefix_evaluation == "":
        return None
    value_stack = []
    prefix_equation = prefix_evaluation.split()
    while prefix_equation:
        el = prefix_equation.pop()
        if el not in ops:
            value_stack.append(int(el))
        else:
            r_val = value_stack.pop()
            l_val = value_stack.pop()
            operation = ops[el]
            value_stack.append(operation(r_val, l_val))

    return value_stack[0]


def to_prefix(equation: str) -> List[str]:
    pass
    token_stack = []
    prefix_tokens = []
    tokens = list(reversed(equation.split()))
    while tokens:
        token = tokens.pop()

    return " ".join(prefix_tokens)


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
