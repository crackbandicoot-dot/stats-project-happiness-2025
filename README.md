# World Happiness Report Statistical Analysis

A comprehensive statistical analysis project examining the World Happiness Report data to identify patterns, regional differences, and socioeconomic factors that influence happiness levels across countries.

## Project Overview

This repository contains a statistical analysis project from Universidad de la Habana, MATCOM (2025-2026) that explores the World Happiness Report dataset with a focus on:

- **Regional Comparison**: Analyzing happiness differences between Nordic countries and Latin America
- **Socioeconomic Factors**: Investigating which factors (GDP, social support, life expectancy, etc.) have the greatest impact on happiness in different regions
- **Data Clustering**: Identifying natural groupings of countries based on their well-being indicators using machine learning techniques
- **Statistical Hypothesis Testing**: Testing hypotheses about happiness variations across regions and populations

## Repository Structure

```
stats-project-happiness-2025/
├── README.md                          # Project documentation
├── data/
│   └── happiness-data.csv             # World Happiness Report dataset
├── docs/
│   └── template.md                    # Documentation template
└── notebooks/
    └── happiness_analysis.ipynb       # Main Jupyter notebook with statistical analysis
```

### Directory Contents

- **`data/`**: Contains the raw World Happiness Report dataset (`happiness-data.csv`) with country-level well-being indicators
- **`docs/`**: Documentation templates and additional project documentation
- **`notebooks/`**: Jupyter notebooks with the complete statistical analysis, including:
  - Exploratory Data Analysis (EDA)
  - Hypothesis testing comparing regions
  - Regression analysis of socioeconomic factors
  - Clustering and Principal Component Analysis (PCA)

## Key Research Questions

1. Is there a significant difference in happiness between Nordic countries and Latin America?
2. Which socioeconomic factors have the greatest weight in each region?
3. Do countries naturally cluster based on their well-being indicators?

## Technologies Used

- **Python 3**: Data analysis and statistical computing
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib & seaborn**: Data visualization
- **scikit-learn**: Machine learning (clustering, dimensionality reduction)
- **scipy & statsmodels**: Statistical testing and modeling
- **Jupyter**: Interactive notebook environment

## Analysis Sections

The main analysis notebook (`happiness_analysis.ipynb`) is organized into the following sections:

1. **Data Loading and Preparation**: Loading and cleaning the World Happiness Report data
2. **Exploratory Data Analysis**: Descriptive statistics and visualizations
3. **Hypothesis Testing**: Comparing happiness metrics between regions
4. **Regression Analysis**: Modeling happiness as a function of socioeconomic factors
5. **Clustering & PCA**: Identifying country groups and reducing data dimensionality
6. **Conclusions**: Summary of findings and insights

## Getting Started

To run this analysis:

1. Ensure you have Python 3 and Jupyter installed
2. Install required dependencies: `pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels`
3. Open the notebook: `jupyter notebook notebooks/happiness_analysis.ipynb`
4. Run the cells to reproduce the analysis

## Dataset

The analysis uses the World Happiness Report dataset, which includes indicators such as:
- Life Ladder (overall happiness score)
- GDP per capita
- Social support
- Healthy life expectancy
- Freedom to make life choices
- Generosity
- Corruption perception
