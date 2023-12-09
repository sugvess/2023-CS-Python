from operator import add, mul, sub, truediv

ops = {"+": add, "-": sub, "*": mul, "/": truediv}
prioritet = {"+": 1, "-": 1, "*": 2, "/": 2}


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


def to_prefix(equation: str) -> str:
    pass
    token_stack = []
    prefix_tokens = []
    for tocen in reversed(equation.split()):
        if tocen not in ops:
            if tocen != "(" and tocen != ")":
                token_stack.append(tocen)
            if tocen == "(":
                while prefix_tokens and prefix_tokens[-1] != ")":
                    token_stack.append(prefix_tokens.pop())
                prefix_tokens.pop()
            if tocen == ")":
                prefix_tokens.append(tocen)
        if tocen in ops:
            while (
                prefix_tokens
                and prefix_tokens[-1] != ")"
                and prioritet[tocen] <= prioritet.get(prefix_tokens[-1], 0)
            ):
                token_stack.append(prefix_tokens.pop())
            prefix_tokens.append(tocen)
    while prefix_tokens:
        token_stack.append(prefix_tokens.pop())

    return " ".join(list(reversed(token_stack)))


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
