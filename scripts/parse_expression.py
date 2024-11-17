import pandas as pd
import os

# Step 1: Parse the sample sheet to filter for PT and STN
sample_sheet = pd.read_csv("gdc_sample_sheet.tsv", sep="\t")
filtered_samples = sample_sheet[sample_sheet["Sample Type"].isin(["Primary Tumor", "Solid Tissue Normal"])]
filtered_samples = filtered_samples[["File ID", "Sample Type"]]
filtered_samples.to_csv("results/filtered_samples.tsv", sep="\t", index=False)

# Step 2: Extract expression values
output_data = []

for _, row in filtered_samples.iterrows():
    file_id, sample_type = row["File ID"], row["Sample Type"]
    expression_file = os.path.join("data", file_id, "*.tsv")
    
    # Load the expression data
    try:
        expression_df = pd.read_csv(expression_file, sep="\t")
        nkx2_row = expression_df[expression_df["gene_id"] == "NKX2-1"]
        tpm_value = nkx2_row.iloc[0, 6]  # Assuming TPM column is 7th (index 6)
        output_data.append([file_id, sample_type, tpm_value])
    except Exception as e:
        print(f"Error processing file {expression_file}: {e}")

expression_df = pd.DataFrame(output_data, columns=["File ID", "Sample Type", "TPM"])
expression_df.to_csv("results/expression_values.tsv", sep="\t", index=False)
