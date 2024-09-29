import numpy as np
import matplotlib.pyplot as plt
#Table 1.4
# Data preparation
years = ['2022', '2023', '2024']

# Standardized Death Rates (SDR)
sdr_males = [11.528, 11.734, 11.046]  # Males SDR
sdr_females = [8.084, 8.171, 7.987]    # Females SDR

# Confidence Intervals (CI)
ci_males = [0.541, 0.537, 0.515]  # Males CI
ci_females = [0.411, 0.406, 0.396] # Females CI

# Create pie charts
plt.figure(figsize=(12, 6))

# First Pie Chart: SDR for Males
plt.subplot(1, 2, 1)
plt.pie(sdr_males, labels=years, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Standardized Death Rates (SDR) - Males (2022 to 2024)')

# Second Pie Chart: SDR for Females
plt.subplot(1, 2, 2)
plt.pie(sdr_females, labels=years, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Standardized Death Rates (SDR) - Females (2022 to 2024)')

# Show the plot for SDR
plt.tight_layout()
plt.show()

# Create pie charts for Confidence Intervals
plt.figure(figsize=(12, 6))

# First Pie Chart: CI for Males
plt.subplot(1, 2, 1)
plt.pie(ci_males, labels=years, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Confidence Intervals (+/-) - Males (2022 to 2024)')

# Second Pie Chart: CI for Females
plt.subplot(1, 2, 2)
plt.pie(ci_females, labels=years, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Confidence Intervals (+/-) - Females (2022 to 2024)')

# Show the plot for CI
plt.tight_layout()
plt.show()
