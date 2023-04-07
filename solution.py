import pandas as pd
import numpy as np
import scipy.stats as st

from scipy.stats import norm


chat_id = 611202811 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    t = 53
    alpha = 1 - p
    loc = sum(x)/n
    
    
    z1 = st.gamma.ppf((1+p)/2, a = n, scale = 1/n)
    z2 = st.gamma.ppf((1-p)/2, a = n, scale = 1/n)

    return loc/(t*t) + 1/(2*t*t) + z1/(t*t), \
    loc/(t*t) + 1/(2*t*t) + z2/(t*t)

