import pandas as pd

# Buat contoh dataset dengan nilai yang hilang dan outlier
data = {
    'A': [10, 20, 30, None, 40, 50, 60],
    'B': [100, 200, 300, 400, 500, 600, 700]
}

df = pd.DataFrame(data)

# Data Cleaning - Mengatasi nilai yang hilang
# Menghapus baris dengan nilai yang hilang
df_cleaned = df.dropna()

# Mengisi nilai yang hilang dengan mean dari kolom A
mean_A = df['A'].mean()
df['A'] = df['A'].fillna(mean_A)

print("Dataset setelah data cleaning - mengatasi nilai yang hilang:")
print(df)

# Data Cleaning - Mengatasi outlier
# Deteksi outlier dengan Z-Score
from scipy.stats import zscore
z_scores = zscore(df)
outliers = (z_scores > 3).any(axis=1)

# Hapus baris dengan outlier
df_cleaned = df[~outliers]

print("\nDataset setelah data cleaning - mengatasi outlier:")
print(df_cleaned)
