import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the expression data
expression_data = pd.read_csv("results/expression_values.tsv", sep="\t")

# Prepare data for the plot
expression_data["Log2(TPM+1)"] = expression_data["TPM"].apply(lambda x: np.log2(x + 1))
print(expression_data.isnull().sum())
print(expression_data.groupby("Sample Type").size())

# Generate the boxplot
plt.figure(figsize=(8, 6))
print(expression_data.head())
sns.boxplot(data=expression_data, x="Sample Type", y="Log2(TPM+1)", palette="Set2")
plt.show()

# Add title and labels
plt.title("Expression of NKX2-1 in PT and STN Conditions", fontsize=14)
plt.xlabel("Sample Type", fontsize=12)
plt.ylabel("Log2(TPM + 1)", fontsize=12)

# Save the plot
plt.savefig("results/boxplot.png")
plt.close()
