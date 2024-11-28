from collections import Counter

# Fungsi untuk menghitung Gini Impurity
def gini_impurity(labels):
    total_count = len(labels)
    if total_count == 0:
        return 0
    label_counts = Counter(labels)
    impurity = 1 - sum((count / total_count) ** 2 for count in label_counts.values())
    return impurity

# Contoh dataset
data = [
    {"Warna": "Merah", "Buah": "Apel"},
    {"Warna": "Hijau", "Buah": "Apel"},
    {"Warna": "Kuning", "Buah": "Lemon"},
    {"Warna": "Kuning", "Buah": "Lemon"},
    {"Warna": "Oranye", "Buah": "Jeruk"},
    {"Warna": "Hijau", "Buah": "Apel"},
    {"Warna": "Oranye", "Buah": "Jeruk"}
]

# Ekstrak label "Buah"
labels = [item["Buah"] for item in data]

# Hitung Gini Impurity untuk seluruh dataset
gini = gini_impurity(labels)
print(f'Gini Impurity untuk seluruh dataset: {gini:.4f}')

# Hitung Gini Impurity untuk subset berdasarkan warna
subset_hijau = [item["Buah"] for item in data if item["Warna"] == "Hijau"]
subset_kuning = [item["Buah"] for item in data if item["Warna"] == "Kuning"]
subset_oranye = [item["Buah"] for item in data if item["Warna"] == "Oranye"]

gini_hijau = gini_impurity(subset_hijau)
gini_kuning = gini_impurity(subset_kuning)
gini_oranye = gini_impurity(subset_oranye)

print(f'Gini Impurity untuk subset Hijau: {gini_hijau:.4f}')
print(f'Gini Impurity untuk subset Kuning: {gini_kuning:.4f}')
print(f'Gini Impurity untuk subset Oranye: {gini_oranye:.4f}')
