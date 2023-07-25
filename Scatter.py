import seaborn as sns
import matplotlib.pyplot as plt

# Muat dataset tips dari library Seaborn
tips = sns.load_dataset('tips')

# Plot scatter plot untuk melihat hubungan antara 'total_bill' dan 'tip'
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Scatter Plot of Total Bill vs Tip')
plt.show()
