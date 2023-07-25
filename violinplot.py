import seaborn as sns
import matplotlib.pyplot as plt

# Muat dataset tips dari library Seaborn
tips = sns.load_dataset('tips')

# Plot violin plot untuk melihat distribusi data 'total_bill' berdasarkan 'day' (hari) dan 'sex' (jenis kelamin)
plt.figure(figsize=(8, 6))
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.title('Violin Plot of Total Bill by Day and Gender')
plt.show()
