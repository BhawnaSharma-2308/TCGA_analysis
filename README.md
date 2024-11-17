Input files - gdc_sample_sheet.tsv, gdc_manifest.txt, and tcga_data.tar.gz

Step 1 - the Snakemake file

Step 2 - parse_expression.py script to parse the sample sheet and extraction of expression data for NKX2-1.

Step 3 - generate-boxplot.py script for generating a boxplot for the extracted expression data. 

Final command - snakemake --cores 1

Expected Outputs - 
1. results/filtered_samples.tsv, conatins File ID and Sample Type for PT and STN.
2. results/expression_values.tsv, contains TPM values for NKX2-1.
3. results/boxplot.png, Boxplot comparing NKX2-1 expression between PT and STN conditions. 
