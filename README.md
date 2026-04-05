# 💳 Credit Card Fraud Analysis - EDA

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-1.6-green?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12-orange?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-red?style=for-the-badge)

---

## 📖 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the **Credit Card Fraud dataset**.  
The goal is to analyze patterns in transactions, visualize distributions, and detect anomalies related to fraudulent transactions.

- **Dataset:** Credit Card transactions (V1-V28 features, Amount, Time, Class)  
- **Target:** Class (0 = Normal, 1 = Fraud)  
- **Type of Analysis:** Statistical summary, visual exploration, correlation analysis

---

## 🛠️ Features / Analysis

1. **Data Overview**
   - Dataset shape and summary statistics
   - Checking for missing values

2. **Class Distribution**
   - Count of normal vs fraudulent transactions
   - Visualization using bar plot

3. **Correlation Analysis**
   - Correlation heatmap of all features
   - Identify relationships between features

4. **Transaction Amount Analysis**
   - Boxplot of Amount by Class
   - Detect outliers in fraud transactions

5. **Feature Distributions**
   - Histograms with KDE for all numerical features (`V1-V28`, `Amount`, `Time`)

---

> **Note:** The dataset `creditcard.csv` is not included due to size and privacy. Please download it from [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) and place it in the `data/` folder.

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone  https://github.com/Nersisiian/Credit_Card_Fraud_Analysis.git
cd credit_card_fraud_analysis

2. Install dependencies:
pip install -r requirements.txt

3. Launch Jupyter Notebook:
jupyter notebook
4. Open notebooks/EDA.ipynb and run all cells.
📊 Example Visualizations
Class Distribution

(example)
Correlation Heatmap

(example)
Transaction Amount Boxplot

(example)
🔧 Tools & Libraries
Python 3
Pandas, NumPy
Matplotlib, Seaborn
Jupyter Notebook
📈 Outcome
Understanding data structure, distribution, and correlations
Highlighted anomalies and insights in fraudulent transactions
Ready dataset for further modeling / machine learning (fraud detection)
📝 Author

Your Name – Data Science & Machine Learning Enthusiast
