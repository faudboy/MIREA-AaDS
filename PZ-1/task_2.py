from math import asin, sqrt, log
print("тип ввода: 0 1 0.0001 (начало конец погрешность)")
def x_k(a, b): return a - (f4(a)*(b - a))/(f4(b) - f4(a)) # функция для поиск методом хорд
def f4(x): return sqrt(1-0.4*x**2) - asin(x) # вариант 4
a, b, ep_s = map(float, input().split())
k, x_k0, x_k1  = 0, a, x_k(a, b)

while abs(x_k1 - x_k0) > ep_s: # проверяем на соблюдение погрешность
    k += 1
    x_k0 = x_k1
    if f4(x_k1)*f4(b) > 0: b = x_k1
    else: a = x_k1
    x_k1 = x_k(a, b)
    if f4(x_k1) == 0: break

print(f"{k} steps, корень равен {x_k1:.{int(-log(ep_s, 10))}f} с погрешностью {ep_s}")
