import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = "../data/creditcard.csv"

if not os.path.exists(data_path):
    print("Файл creditcard.csv не найден в папке data/")
    exit()

df = pd.read_csv(data_path)

print("Форма датасета:", df.shape)
print("\nПропуски:\n", df.isnull().sum())

print("\nСтатистики:\n", df.describe())

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], bins=50, kde=True)
    plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig(f"../figures/hist_{col}.png")
    plt.close()

plt.figure(figsize=(12,10))
correlation = df.corr()
sns.heatmap(correlation, cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("../figures/heatmap.png")
plt.close()

print("EDA завершено! Графики сохранены в папке figures/")