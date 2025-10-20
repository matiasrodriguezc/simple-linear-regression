# Simple Linear Regression Examples in Python

This repository contains examples of simple linear regression implemented in Python using two popular libraries: **Statsmodels** and **Scikit-learn**. The goal is to demonstrate both statistical analysis and machine learning approaches to solving the same problem.

-----

## 📂 Scripts Overview

The project is divided into two parts based on the library used.

### 1\. Statsmodels Implementations (Statistical Approach)

These scripts are ideal for in-depth statistical analysis, providing detailed summaries of the regression results (coefficients, R-squared, p-values, etc.).

  * **`real_estate_price_regression_statsmodels.py`**: Predicts real estate prices based on property size.

      * **Dataset**: `real_estate_price_size.csv`
      * **Features (X)**: `size`
      * **Target (Y)**: `price`

  * **`sat_gpa_regression_statsmodels.py`**: Predicts a student's GPA based on their SAT score.

      * **Dataset**: `1.01. Simple linear regression.csv`
      * **Features (X)**: `SAT`
      * **Target (Y)**: `GPA`

### 2\. Scikit-learn Implementations (Machine Learning Approach)

These scripts use `scikit-learn`, the industry standard for machine learning in Python. The focus here is on model fitting and prediction.

  * **`real_estate_price_regression_sklearn.py`**: A machine learning model to predict real estate prices.

      * **Dataset**: `real_estate_price_size.csv`
      * **Features (X)**: `size`
      * **Target (Y)**: `price`

  * **`sat_gpa_regression_sklearn.py`**: A machine learning model to predict GPA from SAT scores.

      * **Dataset**: `1.01. Simple linear regression.csv`
      * **Features (X)**: `SAT`
      * **Target (Y)**: `GPA`

-----

## 🛠️ Requirements

You will need Python 3 and the following libraries to run these scripts:

  * **pandas**: For data manipulation and loading CSV files.
  * **numpy**: For numerical operations.
  * **matplotlib**: For creating visualizations.
  * **statsmodels**: For in-depth statistical modeling.
  * **seaborn**: For enhanced data visualization.
  * **scikit-learn**: For building machine learning models.

-----

## ⚙️ Installation

1.  **Clone the repository** (or download the files to a local directory).

2.  **Install all required libraries** by running the following command in your terminal:

    ```bash
    python3 -m pip install pandas numpy matplotlib statsmodels seaborn scikit-learn
    ```

-----

## ▶️ How to Run

Navigate to the project directory in your terminal and run the desired script.

**For the Statsmodels examples:**

```bash
# Real estate example
python3 real_estate_price_regression_statsmodels.py

# SAT/GPA example
python3 sat_gpa_regression_statsmodels.py
```

**For the Scikit-learn examples:**

```bash
# Real estate example
python3 real_estate_price_regression_sklearn.py

# SAT/GPA example
python3 sat_gpa_regression_sklearn.py
```

Each script will either print a detailed statistical summary to the console (Statsmodels) or perform model fitting and show how to make predictions (Scikit-learn), followed by a plot visualizing the data and the regression line.
