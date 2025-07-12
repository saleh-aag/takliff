
def f(x):
    return (x - 1)**2 + 2

def df(x):
    return 2 * (x - 1)

# پارامترهای الگوریتم
x = 3.0          # نقطه شروع
learning_rate = 0.1
epsilon = 1e-6   # شرط توقف
max_iterations = 1000
iteration = 0
uu = 0

# اجرای گرادیان نزولی
for iteration in range(max_iterations):
    gradient = df(x)
    x_new = x - learning_rate * gradient
    
    # بررسی همگرایی
    if abs(x_new - x) < epsilon:
        break
    
    x = x_new

# نمایش نتایج
print(f"--- result ---")
print(f" Minimum found at x = {x:.6f}")
print(f" Function value at minimum = {f(x):.6f}")
print(f"tedad tekrar : {iteration + 1}")