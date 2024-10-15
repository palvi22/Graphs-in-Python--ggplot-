import numpy as np
import matplotlib.pyplot as plt
#table 1.2
# Data preparation 
diseases = ['COVID-19', 'Respiratory Diseases', 'Influenza and Pneumonia','Pneumonia', 'Chronic Lower Respiratory Conditions', 'Cancer']


total_deaths = {
    'COVID-19': [163, 241, 104],
    'Respiratory Diseases': [228, 234, 271],
    'Influenza and Pneumonia': [43, 38, 57],
    'Pneumonia': [43, 36, 48],
    'Chronic Lower Respiratory Conditions': [119, 125, 144],
    'Cancer': [938, 960, 971]
}

years = ['2022', '2023', '2024']
#This function is extracting the counts from the list
deaths_per_year = np.array([[total_deaths[disease][0] for disease in diseases],
                            [total_deaths[disease][1] for disease in diseases], 
                            [total_deaths[disease][2] for disease in diseases]])


bar_width = 0.2
ind = np.arange(len(diseases))


plt.bar(ind - bar_width, deaths_per_year[0], width=bar_width, label='2022', color='green')
plt.bar(ind, deaths_per_year[1], width=bar_width, label='2023', color='orange')
plt.bar(ind + bar_width, deaths_per_year[2], width=bar_width, label='2024', color='blue')

plt.xlabel('Diseases', fontweight='bold')
plt.ylabel('Total Deaths', fontweight='bold')
plt.title('Total Deaths by Disease in Australia (2022-2024)', fontweight='bold')
plt.xticks(ind, diseases)


plt.legend()


plt.tight_layout()
plt.show()
 