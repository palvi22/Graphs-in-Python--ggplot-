import matplotlib.pyplot as plt
import numpy as np

#garph 1.1 part 3 :
# graph of country wise distribution 
# Data for the mortality ratios for the six states across 2022, 2023, and 2024
states = ['New South Wales', 'Victoria', 'Queensland', 'South Australia', 'Western Australia', 'Tasmania']
mortality_2022 = [1203, 832, 633, 252, 283, 70]
mortality_2023 = [1115, 874, 723, 272, 341, 85]
mortality_2024 = [1087, 821, 741, 296, 323, 112]


bar_width = 0.25
x = np.arange(len(states))
fig, ax = plt.subplots(figsize=(10, 6))


bar1 = ax.bar(x - bar_width, mortality_2022, bar_width, label='2022')
bar2 = ax.bar(x, mortality_2023, bar_width, label='2023')
bar3 = ax.bar(x + bar_width, mortality_2024, bar_width, label='2024')


ax.set_xlabel('State')
ax.set_ylabel('Mortality Numbers')
ax.set_title('Mortality Numbers for AustralianState(2022-2024)')
ax.set_xticks(x)
ax.set_xticklabels(states)
ax.legend()


plt.tight_layout()
plt.show()
