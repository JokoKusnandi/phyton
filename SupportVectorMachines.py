# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Muat dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Pisahkan data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat model Support Vector Machines
model = SVC(kernel='linear')

# Latih model dengan data latih
model.fit(X_train, y_train)

# Lakukan prediksi dengan data uji
y_pred = model.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Tampilkan hasil evaluasi
print("Akurasi:", accuracy)
print("Laporan Klasifikasi:\n", report)
print("Confusion Matrix:\n", conf_matrix)
