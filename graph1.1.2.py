import matplotlib.pyplot as plt
import numpy as np

# table 1.1 Praviosnal mortality data graph contains the distinguish male and  female ratio in the compressed bar graph
weeks = [f'Week {i+1}' for i in range(21)]  

male_deaths_2024 = [100, 150, 130, 120, 160, 140, 135, 145, 150, 155, 145, 150, 135, 140, 155, 160, 140, 130, 120, 150, 140]
female_deaths_2024 = [120, 140, 110, 115, 150, 130, 125, 140, 145, 150, 130, 140, 125, 130, 150, 155, 130, 120, 115, 140, 130]



male_deaths_2023 = [90, 140, 120, 110, 130, 115, 120, 125, 130, 135, 125, 130, 120, 125, 135, 140, 125, 115, 110, 130, 120]
female_deaths_2023 = [110, 130, 100, 105, 140, 120, 115, 130, 135, 140, 120, 130, 110, 115, 140, 145, 120, 110, 105, 130, 115]

male_deaths_2022 = [80, 130, 110, 100, 120, 105, 110, 115, 120, 125, 115, 120, 110, 115, 125, 130, 115, 105, 100, 120, 110]
female_deaths_2022 = [100, 120, 90, 95, 130, 110, 105, 120, 125, 130, 110, 120, 100, 105, 130, 135, 110, 100, 95, 120, 105]

bar_width = 0.1 
x = np.arange(len(weeks))

fig, ax = plt.subplots(figsize=(18, 8))

bars1_male = ax.bar(x - bar_width, male_deaths_2024, width=bar_width, color='blue',label='2024 Male')
bars1_female = ax.bar(x - bar_width, female_deaths_2024, width=bar_width, bottom=male_deaths_2024, color='lightblue', label='2024 Female')

bars2_male = ax.bar(x, male_deaths_2023, width=bar_width, color='green', label='2023 Male')
bars2_female = ax.bar(x, female_deaths_2023, width=bar_width, bottom=male_deaths_2023, color='lightgreen', label='2023 Female')

bars3_male = ax.bar(x + bar_width, male_deaths_2022, width=bar_width, color='red', label='2022 Male')
bars3_female = ax.bar(x + bar_width, female_deaths_2022, width=bar_width, bottom=male_deaths_2022, color='pink', label='2022 Female')

ax.set_xlabel('Weeks', fontsize=12)
ax.set_ylabel('Number of Deaths', fontsize=12)
ax.set_title('Weekly Deaths Comparison by Year and Gender (Stacked) 21Weeks',fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(weeks, rotation=45)
ax.legend()

plt.tight_layout()
plt.show()
