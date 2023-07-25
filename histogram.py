import seaborn as sns
import matplotlib.pyplot as plt

# Muat dataset tips dari library Seaborn
tips = sns.load_dataset('tips')

# Plot histogram untuk melihat distribusi data kolom 'total_bill'
plt.figure(figsize=(8, 6))
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.xlabel('Total Bill')
plt.ylabel('Count')
plt.title('Histogram of Total Bill')
plt.show()
