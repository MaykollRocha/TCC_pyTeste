import cmath
import math
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Função base para calcular potência de 10
def base(x, y):
    if x == 0 or y == 0:
        return 1
    return 10 ** max(math.ceil(math.log10(x) / 3), math.ceil(math.log10(y) / 3))