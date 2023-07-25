import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Sample data for illustration
data = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Count': [30, 20, 25, 35, 15, 25]
})

# Create a contingency table
contingency_table = pd.pivot_table(data, values='Count', index='Category', aggfunc=np.sum)

# Chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Print the test result
print("Chi-square test result:")
print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")

# Visualization
plt.bar(data['Category'], data['Count'])
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Sample Data')
plt.show()
