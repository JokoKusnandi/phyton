import seaborn as sns
import matplotlib.pyplot as plt

# Muat dataset tips dari library Seaborn
tips = sns.load_dataset('tips')

# Plot pair plot untuk melihat hubungan antara beberapa fitur
sns.pairplot(tips)
plt.show()
