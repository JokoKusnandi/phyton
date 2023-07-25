import seaborn as sns
import matplotlib.pyplot as plt

# Muat dataset tips dari library Seaborn
tips = sns.load_dataset('tips')

# Melihat beberapa baris pertama dari dataset
print(tips.head())

# Visualisasi Distribusi Data dengan Histogram
plt.figure(figsize=(8, 6))
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.xlabel('Total Bill')
plt.ylabel('Count')
plt.title('Histogram of Total Bill')
plt.show()

# Visualisasi Hubungan antara dua fitur dengan Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Scatter Plot of Total Bill vs Tip')
plt.show()

# Visualisasi Hubungan antara beberapa fitur dengan Pair Plot
sns.pairplot(tips, hue='sex')
plt.show()

# Visualisasi Distribusi Data dengan Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=tips)
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.title('Box Plot of Total Bill by Day')
plt.show()

# Visualisasi Distribusi Data dengan Violin Plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.title('Violin Plot of Total Bill by Day and Gender')
plt.show()
