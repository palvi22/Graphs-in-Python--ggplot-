# Provisional Mortality Analysis of Australia (2022-2024)

This project analyzes provisional mortality data in Australia for the period between
2022 and 2024 using Python and `ggplot` for visualizations. The analysis includes a 
range of graphs and insights into trends over time.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Graphs Included](#graphs-included)
- [Setup Instructions](#setup-instructions)
- [Future Enhancements](#future-enhancements)

## Introduction
This project aims to visualize and explore mortality trends in Australia from 2022 
to 2024. The dataset includes monthly records of deaths and is processed to provide
insights into variations over time.

## Features
- Data cleaning and processing.
- Multiple mortality trend visualizations using `ggplot`.
- Comparative analysis for different years.
  
## Technologies
- **Python**: Core language for data analysis and visualization.
- **Pandas**: For data manipulation.
- **Matplotlib** and **ggplot**: Libraries used for creating graphs.

## Graphs Included
- Monthly mortality trends.
- Year-on-year comparisons.
- Seasonal variations in mortality rates.

## Setup Instructions

-1. Clone the repository:

   git clone https://github.com/your-username/provisional-mortality-australia.git

-2.Navigate to the project directory:

cd provisional-mortality-australia

-3.Install dependencies:

pip install -r requirements.txt
Add your dataset to the data folder as mortality_data.csv.

-Run the Python script to generate graphs:

python scripts/mortality_analysis.py

## requirements.txt

- pandas
- matplotlib
- plotnine
