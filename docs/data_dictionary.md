# Happiness Data Dictionary

Welcome to the project! This document explains the contents of the `data/happiness-data-clean.csv` file. This dataset captures how happy people perceive themselves to be in various countries around the world, along with factors that might contribute to that happiness.

## File Overview

- **File Name:** `happiness-data-clean.csv`
- **Location:** `data/` folder
- **Format:** CSV (Comma Separated Values)

## Column Descriptions

Here is a breakdown of what each column in the dataset represents:

### 1. Country name
- **Meaning:** The name of the nation being surveyed.
- **Example:** Finland, Denmark, Iceland.

### 2. Ladder score
- **Meaning:** The main "Happiness Score". It is based on the Cantril Ladder question, where respondents rate their current life on a scale from 0 to 10.
- **Scale:** 
    - **10**: Best possible life.
    - **0**: Worst possible life.
- **Example:** A score of `7.804` indicates a very high level of reported happiness.

### 3. Logged GDP per capita
- **Meaning:** A measure of the country's economic output per person.
- **Details:** The "Logged" part means the value has been transformed using a logarithm. This is standard in economics to compare countries with vastly different income levels (money matters more to happiness at lower income levels than at very high ones).
- **Interpretation:** Higher values generally mean a wealthier country.

### 4. Social support
- **Meaning:** The national average of the binary responses (0 or 1) to the question: "If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them?"
- **Scale:** 0 to 1.
- **Interpretation:** Higher values closer to 1 mean more people feel they have a support system.

### 5. Healthy life expectancy
- **Meaning:** The average number of years a newborn infant would expect to live in "good health".
- **Scale:** In years.
- **Example:** `71.150` means the average person is expected to live over 71 years in good health.

### 6. Freedom to make life choices
- **Meaning:** The national average of responses to the question: "Are you satisfied or dissatisfied with your freedom to choose what you do with your life?"
- **Scale:** 0 to 1.
- **Interpretation:** Higher values mean citizens feel more free to live life as they choose.

### 7. Generosity
- **Meaning:** Is a measure derived from how many people donated money to charity recently, adjusted for GDP per capita.
- **Note:** You might see negative values here (e.g., `-0.019`). This is because it's a "residual" value—it compares the actual generosity to what we would expect given the country's GDP. A positive value means higher generosity than expected; a negative value means lower.

### 8. Perceptions of corruption
- **Meaning:** The average of binary answers to two questions: "Is corruption widespread throughout the government?" and "Is corruption widespread within businesses?"
- **Scale:** 0 to 1.
- **Interpretation:** Higher values (closer to 1) indicate that people perceive **more** corruption. Lower values indicate **less** corruption.

## Tips for Beginners
- If you are analyzing this data, `Ladder score` is usually your target variable (what you are trying to predict or explain).
- The other columns are "features" or predictors.
- Watch out for `Perceptions of corruption`—unlike most other positive metrics here (where higher is better), a higher corruption score is generally considered a negative thing for society.

Happy analyzing!
