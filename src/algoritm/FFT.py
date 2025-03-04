class FFTMultiplier:
    def __init__(self):
        self.steps = {}

    def log_step(self, step_name, data):
      if isinstance(data, list) and all(isinstance(i, (complex, float, int)) for i in data):
          self.steps[step_name] = self.print_matrix(data, step_name)
      else:
          self.steps[step_name] = str(data)  # Convertendo para string para evitar erros


    def print_matrix(self, matrix, name):
        output = f"\n{name}:\n"
        for i, value in enumerate(matrix):
            if isinstance(value, complex):
                output += f"  [{i}] {value.real:.2f} + {value.imag:.2f}j\n"
            else:
                output += f"  [{i}] {value:.2f}\n"
        output += "\n"
        return output

    def FFT(self, a, omega):
        n = len(a)
        if n == 1:
            return a

        a_even = self.FFT(a[0::2], omega * omega)
        a_odd = self.FFT(a[1::2], omega * omega)

        y = [0] * n
        x = 1

        for i in range(n // 2):
            y[i] = a_even[i] + x * a_odd[i]
            y[i + n // 2] = a_even[i] - x * a_odd[i]
            x *= omega

        return y

    def inverse_FFT(self, y, omega):
        n = len(y)
        if n == 1:
            return y

        y_even = self.inverse_FFT(y[0::2], omega * omega)
        y_odd = self.inverse_FFT(y[1::2], omega * omega)

        a = [0] * n
        x = 1

        for i in range(n // 2):
            a[i] = (y_even[i] + x * y_odd[i]) / 2
            a[i + n // 2] = (y_even[i] - x * y_odd[i]) / 2
            x *= omega

        return a

    def pad_coefficients(self, a, size):
        return a + [0] * (size - len(a))

    def multiply_polynomials(self, p, q):
        n = 1
        while n < len(p) + len(q) - 1:
            n *= 2

        p = self.pad_coefficients(p, n)
        q = self.pad_coefficients(q, n)

        omega = cmath.exp(2j * cmath.pi / n)
        y = self.FFT(p, omega)
        z = self.FFT(q, omega)
        self.log_step("3️⃣ Multiplicação no domínio da frequência - FFT(A(x))", y)
        self.log_step("3️⃣ Multiplicação no domínio da frequência - FFT(B(x))", z)

        m = [y[i] * z[i] for i in range(n)]
        self.log_step("3️⃣ Multiplicação no domínio da frequência", m)
        
        omega_inv = cmath.exp(-2j * cmath.pi / n)
        result = self.inverse_FFT(m, omega_inv)
        self.log_step("4️⃣ Aplicação da IFFT para recuperar os coeficientes", result)

        return [round(x.real) for x in result]

    def integer_to_polynomial(self, x, base=10):
        coeffs = []
        while x:
            coeffs.append(x % base)
            x //= base
        return coeffs or [0]

    def polynomial_to_integer(self, coeffs, base=10):
        result = 0
        power = 1
        for coef in coeffs:
            result += coef * power
            power *= base
        return result

    def fft_multiply_integers(self, x, y, base=10):
        p = self.integer_to_polynomial(x, base)
        q = self.integer_to_polynomial(y, base)
        self.log_step("1️⃣ Representação como polinômios", f"A(x): {p}, B(x): {q}")

        product_coeffs = self.multiply_polynomials(p, q)
        result = self.polynomial_to_integer(product_coeffs, base)
        self.log_step("5️⃣ Conversão para número final", f"Resultado da multiplicação de {x} por {y}: {result} {'certo' if (result == x*y) else 'errado'}")
        
        return result

    def get_steps(self):
        return "\n".join(self.steps.values())