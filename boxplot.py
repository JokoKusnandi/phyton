import seaborn as sns
import matplotlib.pyplot as plt

# Muat dataset tips dari library Seaborn
tips = sns.load_dataset('tips')

# Plot box plot untuk melihat distribusi data 'total_bill' pada setiap 'day' (hari)
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=tips)
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.title('Box Plot of Total Bill by Day')
plt.show()
