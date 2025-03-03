import cmath
import math
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def print_matrix(matrix, name):
    st.write(f"\n{name}:")
    for i, value in enumerate(matrix):
        if isinstance(value, complex):
            st.write(f"  [{i}] {value.real:.2f} + {value.imag:.2f}j")
        else:
            st.write(f"  [{i}] {value:.2f}")
    st.write("\n")

def FFT(a, omega):
    n = len(a)
    if n == 1:
        return a

    a_even = FFT(a[0::2], omega * omega)
    a_odd = FFT(a[1::2], omega * omega)

    y = [0] * n
    x = 1

    for i in range(n // 2):
        y[i] = a_even[i] + x * a_odd[i]
        y[i + n // 2] = a_even[i] - x * a_odd[i]
        x *= omega

    return y

def inverse_FFT(y, omega):
    n = len(y)
    if n == 1:
        return y

    y_even = inverse_FFT(y[0::2], omega * omega)
    y_odd = inverse_FFT(y[1::2], omega * omega)

    a = [0] * n
    x = 1

    for i in range(n // 2):
        a[i] = (y_even[i] + x * y_odd[i]) / 2
        a[i + n // 2] = (y_even[i] - x * y_odd[i]) / 2
        x *= omega

    return a

def pad_coefficients(a, size):
    return a + [0] * (size - len(a))

def multiply_polynomials(p, q):
    n = 1
    while n < len(p) + len(q) - 1:
        n *= 2

    p = pad_coefficients(p, n)
    q = pad_coefficients(q, n)

    omega = cmath.exp(2j * cmath.pi / n)
    y = FFT(p, omega)
    z = FFT(q, omega)
    st.write("\n3️⃣ Multiplicação no domínio da frequência:")
    
    col1, col2 = st.columns(2)

    with col1:
        print_matrix(y, "FFT(A(x))")

    with col2:
        print_matrix(z, "FFT(B(x))")

    m = [y[i] * z[i] for i in range(n)]
    print_matrix(m, "\n3️⃣ Multiplicação no domínio da frequência:")
    omega_inv = cmath.exp(-2j * cmath.pi / n)
    result = inverse_FFT(m, omega_inv)
    print_matrix(result, "\n4️⃣ Aplicação da IFFT para recuperar os coeficientes:")

    # Plotting FFT and IFFT
    plot_fft_ifft(y, m, result)

    return [round(x.real) for x in result]

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

def fft_multiply_integers(x, y, base=10):
    if x == 1 and y == 1:
        return 1
    p = integer_to_polynomial(x, base)
    q = integer_to_polynomial(y, base)
    st.write("1️⃣ Representação como polinômios:")
    st.write(f"A(x): {p}")
    st.write(f"B(x): {q}")

    product_coeffs = multiply_polynomials(p, q)

    return polynomial_to_integer(product_coeffs, base)

def plot_fft_ifft(fft_result, fft_multiplied, ifft_result):
    # FFT Magnitude Plot
    fft_magnitude = [abs(x) for x in fft_result]
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(fft_magnitude)
    plt.title('Magnitude da FFT')
    plt.xlabel('Índice')
    plt.ylabel('Magnitude')

    # IFFT Magnitude Plot
    ifft_magnitude = [abs(x) for x in ifft_result]
    plt.subplot(1, 2, 2)
    plt.plot(ifft_magnitude)
    plt.title('Magnitude da IFFT')
    plt.xlabel('Índice')
    plt.ylabel('Magnitude')

    st.pyplot(plt)

# Interface com o usuário no Streamlit
st.title("Multiplicação de Inteiros via FFT")

a = st.number_input("Digite o primeiro número:", min_value=1)
b = st.number_input("Digite o segundo número:", min_value=1)

base = 10 ** max(math.ceil(math.log(a, 10) / 3), math.ceil(math.log(b, 10) / 3))

if st.button("Calcular"):
    result = fft_multiply_integers(a, b, base)
    st.write("\n5️⃣ Conversão para número final:")
    st.write(f"Resultado da multiplicação de {a} por {b}: {result} {'certo' if (result == a * b) else 'errado'}")