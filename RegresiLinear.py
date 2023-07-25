# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Data yang berlabel (contoh: data tinggi badan dan berat badan)
tinggi_badan = np.array([160, 165, 170, 175, 180, 185]).reshape(-1, 1)
berat_badan = np.array([60, 65, 70, 75, 80, 85])

# Pisahkan data menjadi data latih dan data uji
tinggi_train, tinggi_test, berat_train, berat_test = train_test_split(tinggi_badan, berat_badan, test_size=0.2, random_state=42)

# Buat model Regresi Linier
model = LinearRegression()

# Latih model dengan data latih
model.fit(tinggi_train, berat_train)

# Lakukan prediksi dengan data uji
berat_prediksi = model.predict(tinggi_test)

# Plot data dan garis regresi
plt.scatter(tinggi_badan, berat_badan, color='blue', label='Data Asli')
plt.plot(tinggi_test, berat_prediksi, color='red', label='Regresi Linier')
plt.xlabel('Tinggi Badan')
plt.ylabel('Berat Badan')
plt.legend()
plt.show()
