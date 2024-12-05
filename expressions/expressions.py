import numbers

class Expression:
    """Node of an expression tree."""

    def __init__(self, *operands):
        converted_operands = tuple(
            [Number(op) if isinstance(op, numbers.Number)
             else op for op in operands]
                           )
        self.operands = converted_operands

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return Add(self, other)
    
    def __radd__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return other + self
    
    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return Sub(self, other)
    
    def __rsub__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return other - self
    
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return Mul(self, other)

    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return other * self
    
    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return Div(self, other)

    def __rtruediv__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return other / self
    
    def __pow__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return Pow(self, other)

    def __rpow__(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return other ** self


class Operator(Expression):
    def __repr__(self):
        return type(self).__name__ + repr(self.operands)

    def __str__(self):
        operand1 = self.operands[0]
        operand2 = self.operands[1]
        operand_str1 = operand1.__str__()
        operand_str2 = operand2.__str__()

        if operand1.priority < self.priority:
            operand_str1 = f"({operand1.__str__()})"
        if operand2.priority < self.priority:
            operand_str2 = f"({operand2.__str__()})"

        return " ".join([operand_str1, self.symbol, operand_str2])


class Add(Operator):
    symbol = "+"
    priority = 1


class Sub(Operator):
    symbol = "-"
    priority = 1


class Mul(Operator):
    symbol = "*"
    priority = 2


class Div(Operator):
    symbol = "/"
    priority = 2


class Pow(Operator):
    symbol = "^"
    priority = 3


class Terminal(Expression):
    def __init__(self, value):
        self.value = value
        self.priority = 4
        super().__init__()
    
    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)


class Number(Terminal):
    def __init__(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError(
                f"Expected a number, instead received {type(value).__name__}"
            )

        super().__init__(value)


class Symbol(Terminal):
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f"Expected a string, instead received {type(value).__name__}"
            )

        super().__init__(value)