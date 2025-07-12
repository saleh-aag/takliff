
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# تولید 30 عدد تصادفی بین 0 تا 100 به عنوان نمرات دانش‌آموزان
np.random.seed(42)  # ثابت کردن seed برای تکرارپذیری
grades = np.random.randint(0, 101, 30).reshape(-1, 1)  #    تبدیل به آرایه 2بعدی با کمک تابع رند 

# اجرای الگوریتم K-Means با 2 خوشه
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(grades)
labels = kmeans.labels_

# نمایش نتایج
plt.figure(figsize=(10, 5))
colors = ['red' if label == 0 else 'blue' for label in labels]
plt.scatter(grades, np.zeros_like(grades), c=colors, s=100, alpha=0.7)
plt.scatter(kmeans.cluster_centers_, [0, 0], c='green', s=300, marker='X', label='Centroids')
plt.title("khooshe bandi =")
plt.xlabel('nomarat(points)')
#
plt.yticks([])
plt.legend()
plt.show()

# خروجی عددی
print("-- out put --")
print(f"point : {grades.flatten()}")
print(f"Cluster centers: {kmeans.cluster_centers_.flatten()}")
print(f"Number of members per cluster =")
print(f" -(red) _ 0 ->cluster : {np.sum(labels == 0)} student")
print(f"-(blue)_ 1 -> cluster: {np.sum(labels == 1)} student")