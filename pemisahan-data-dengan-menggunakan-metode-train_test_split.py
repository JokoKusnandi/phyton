import numpy as np
from sklearn.model_selection import train_test_split

# Contoh data dengan dua fitur (X) dan label (y)
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([0, 1, 0, 1, 0])

# Pisahkan data menjadi data latih (80%) dan data uji (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tampilkan hasil pemisahan data
print("Data Latih (X_train):\n", X_train)
print("Label Latih (y_train):\n", y_train)
print("Data Uji (X_test):\n", X_test)
print("Label Uji (y_test):\n", y_test)
