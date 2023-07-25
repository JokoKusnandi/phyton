# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Data tanpa label (contoh: data tinggi badan)
tinggi_badan = np.array([160, 165, 170, 175, 180, 185]).reshape(-1, 1)

# Buat model k-means dengan 2 kelompok (silakan ubah sesuai kebutuhan)
kmeans = KMeans(n_clusters=2)

# Latih model dengan data
kmeans.fit(tinggi_badan)

# Dapatkan pusat kelompok dan label dari setiap data
pusat_kelompok = kmeans.cluster_centers_
label_kelompok = kmeans.labels_

# Plot data dan pusat kelompok
plt.scatter(tinggi_badan, np.zeros_like(tinggi_badan), c=label_kelompok, cmap='viridis')
plt.scatter(pusat_kelompok, np.zeros_like(pusat_kelompok), marker='X', s=200, c='red')
plt.xlabel('Tinggi Badan')
plt.show()
