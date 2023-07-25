import pandas as pd
import numpy as np
from scipy.stats import f_oneway
import matplotlib.pyplot as plt

# Sample data for illustration
data = pd.DataFrame({
    'Group': ['A'] * 30 + ['B'] * 30 + ['C'] * 30,
    'Value': [np.random.randint(50, 100) for _ in range(30)] +
             [np.random.randint(60, 90) for _ in range(30)] +
             [np.random.randint(70, 100) for _ in range(30)]
})

# ANOVA test
grouped_data = [group['Value'] for name, group in data.groupby('Group')]
f_statistic, p_value = f_oneway(*grouped_data)

# Print the test result
print("ANOVA test result:")
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

# Visualization
data.boxplot('Value', by='Group')
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Sample Data')
plt.suptitle('')  # Remove the default title
plt.show()
