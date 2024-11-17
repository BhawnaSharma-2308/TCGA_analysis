rule all:
    input:
        "results/boxplot.png"

rule untar_data:
    input:
        "tcga_data.tar.gz"
    output:
        directory("data/")
    shell:
        "tar -zxvf {input} -C ./data/"

rule parse_sample_sheet:
    input:
        "gdc_sample_sheet.tsv"
    output:
        "results/filtered_samples.tsv"
    script:
        "scripts/parse_expression.py"

rule extract_expression:
    input:
        sample_sheet="results/filtered_samples.tsv",
        data_dir="data/"
    output:
        "results/expression_values.tsv"
    script:
        "scripts/parse_expression.py"

rule generate_boxplot:
    input:
        "results/expression_values.tsv"
    output:
        "results/boxplot.png"
    script:
        "scripts/generate_boxplot.py"
