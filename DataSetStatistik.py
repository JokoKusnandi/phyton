import pandas as pd

# Buat contoh dataset dengan beberapa fitur dan label kelas
data = {
    'feature1': [10, 20, 30, 40, 50, 60],
    'feature2': [5, 15, 25, 35, 45, 55],
    'class_label': ['A', 'A', 'B', 'B', 'C', 'C']
}

df = pd.DataFrame(data)

# Melihat beberapa baris pertama dari dataset
print("Dataset:")
print(df)

# Menghitung statistik deskriptif untuk setiap fitur
print("\nStatistik Deskriptif:")
print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Standar Deviasi:\n", df.std())
print("Minimum:\n", df.min())
print("Maksimum:\n", df.max())

# Menghitung statistik deskriptif berdasarkan kelas label
print("\nStatistik Deskriptif Berdasarkan Kelas Label:")
print(df.groupby('class_label').mean())
print(df.groupby('class_label').median())
print(df.groupby('class_label').std())
print(df.groupby('class_label').min())
print(df.groupby('class_label').max())
