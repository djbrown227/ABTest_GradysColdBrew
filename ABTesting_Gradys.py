#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
n_samples = 1000
data = {
    "Order #": range(1, n_samples + 1),
    "Service": np.random.choice(["UPS Ground", "UPS SurePost"], n_samples),
    "Was package delivered": np.random.binomial(1, 0.95, n_samples),  # Assume 95% success rate for both services
    "Cost to deliver": np.where(np.random.choice(["UPS Ground", "UPS SurePost"], n_samples) == "UPS Ground", 10, 9)  # 10% cheaper for SurePost
}

df = pd.DataFrame(data)

# Adjust costs to consistently reflect the 10% cheaper rate for SurePost and recalculate savings
df['Cost to deliver'] = np.where(df['Service'] == "UPS Ground", 10, 9)

# Calculate the observed frequencies for hypothesis testing
contingency_table = pd.crosstab(df['Service'], df['Was package delivered'])
chi2, p_value, _, _ = chi2_contingency(contingency_table)

# Calculate cost savings
average_cost_ground = df[df['Service'] == 'UPS Ground']['Cost to deliver'].mean()
average_cost_surepost = df[df['Service'] == 'UPS SurePost']['Cost to deliver'].mean()
cost_savings = (average_cost_ground - average_cost_surepost) * n_samples

# Output results
print("Contingency Table:\n", contingency_table)
print("Chi-square Statistic:", chi2)
print("P-value:", p_value)
print("Average cost per package (UPS Ground):", average_cost_ground)
print("Average cost per package (UPS SurePost):", average_cost_surepost)
print("Estimated cost savings for the sample:", cost_savings)

