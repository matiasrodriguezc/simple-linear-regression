# Simple Linear Regression Examples in Python

This repository contains two basic examples of simple linear regression implemented in Python. Each script demonstrates how to load data, process it, build a regression model, and visualize the results.

-----

## 📂 Scripts Overview

This project includes two main scripts:

1.  **`real_estate_price_regression.py`**: This script performs a simple linear regression to predict real estate prices based on the size of the property.

      * **Dataset**: `real_estate_price_size.csv`
      * **Independent Variable (X)**: `size`
      * **Dependent Variable (Y)**: `price`

2.  **`sat_gpa_regression.py`**: This script uses simple linear regression to predict a student's GPA based on their SAT score.

      * **Dataset**: `1.01. Simple linear regression.csv`
      * **Independent Variable (X)**: `SAT`
      * **Dependent Variable (Y)**: `GPA`

-----

## 🛠️ Requirements

To run these scripts, you will need Python 3 and the following libraries:

  * **pandas**: For data manipulation and loading CSV files.
  * **numpy**: For numerical operations.
  * **matplotlib**: For creating static, animated, and interactive visualizations.
  * **statsmodels**: For estimating and analyzing statistical models.
  * **seaborn**: For making statistical graphics more attractive.

-----

## ⚙️ Installation

1.  **Clone the repository** (or download the files to a local directory).

2.  **Install the required libraries** using pip. Open your terminal and run the following command:

    ```bash
    python3 -m pip install pandas numpy matplotlib statsmodels seaborn
    ```

-----

## ▶️ How to Run

Navigate to the project directory in your terminal and run the scripts using the following commands:

**For the real estate example:**

```bash
python3 real_estate_price_regression.py
```

**For the SAT/GPA example:**

```bash
python3 sat_gpa_regression.py
```

Each script will generate and display a scatter plot with the corresponding regression line. The model summary, which includes statistics like R-squared, coefficients, and p-values, will be printed to the console.
