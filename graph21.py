import numpy as np
import matplotlib.pyplot as plt
#table 1.2
# Data preparation
diseases = ['COVID-19', 'Respiratory Diseases', 'Influenza and Pneumonia',
            'Pneumonia', 'Chronic Lower Respiratory Conditions', 'Cancer']

# Total deaths data for each disease (example values for 2022, 2023, 2024)
total_deaths = {
    'COVID-19': [163, 241, 104],
    'Respiratory Diseases': [228, 234, 271],
    'Influenza and Pneumonia': [43, 38, 57],
    'Pneumonia': [43, 36, 48],
    'Chronic Lower Respiratory Conditions': [119, 125, 144],
    'Cancer': [938, 960, 971]
}

# Prepare data for plotting
years = ['2022', '2023', '2024']
deaths_per_year = np.array([[total_deaths[disease][0] for disease in diseases],
                             [total_deaths[disease][1] for disease in diseases],
                             [total_deaths[disease][2] for disease in diseases]])

# Set the bar width and positions
bar_width = 0.2
ind = np.arange(len(diseases))

# Create the bar plot
plt.bar(ind - bar_width, deaths_per_year[0], width=bar_width, label='2022', color='green')
plt.bar(ind, deaths_per_year[1], width=bar_width, label='2023', color='orange')
plt.bar(ind + bar_width, deaths_per_year[2], width=bar_width, label='2024', color='blue')

# Adding labels and title
plt.xlabel('Diseases', fontweight='bold')
plt.ylabel('Total Deaths', fontweight='bold')
plt.title('Total Deaths by Disease in Australia (2022-2024)', fontweight='bold')
plt.xticks(ind, diseases)

# Adding legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
