def integer_to_polynomial(x, base=10):
    coeffs = []
    while x:
        coeffs.append(x % base)
        x //= base
    return coeffs or [0]

def polynomial_to_integer(coeffs, base=10):
    result = 0
    power = 1
    for coef in coeffs:
        result += coef * power
        power *= base
    return result
