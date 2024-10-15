import matplotlib.pyplot as plt
import pandas as pd

# Graph 1.1 graph 1:
# contains the 3  year data of 21 weeks of no. of deaths   of persons(male and Female)

weeks = [f"Week {i}" for i in range(1, 22)]

#data = pd.read_csv('deaths_deaths.csv')
deaths_in_year_2022 = [3400, 3380, 3350, 3300, 3280, 3310, 3340, 3360, 3270, 3430,3390, 3220, 3340, 3400, 3420, 3350, 3340, 3450, 3400, 3520, 3700]

deaths_in_year_2023 = [3420, 3370, 3330, 3380, 3250, 3290, 3320, 3300, 3220, 3410,3350, 3200, 3360, 3410, 3425, 3345, 3355, 3480, 3430, 3500, 3730]

deaths_in_year_2024 = [3443, 3391, 3341, 3440, 3263, 3326, 3366, 3348, 3275, 3456, 3371, 3240, 3389, 3421, 3442, 3360, 3368, 3498, 3440, 3538, 3757]

plt.style.use('ggplot')

plt.figure(figsize=(10, 6))

plt.plot(weeks, deaths_in_year_2022, label='2022', color='blue', marker='o')
plt.plot(weeks, deaths_in_year_2023, label='2023', color='green',marker='o')
plt.plot(weeks, deaths_in_year_2024, label='2024', color='red', marker='o')


plt.title('Provisional Mortality Statistics (Jan-May, 2022-2024)', fontsize=14)
plt.xlabel('Weeks (Jan-May)', fontsize=12)
plt.ylabel('Number of Deaths (Persons)', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
